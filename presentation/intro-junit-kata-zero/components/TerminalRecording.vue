<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'
import * as AsciinemaPlayer from 'asciinema-player'
import 'asciinema-player/dist/bundle/asciinema-player.css'

const props = defineProps<{ name: string, alt: string, compact?: boolean, short?: boolean }>()
const base = import.meta.env.BASE_URL
const { $nav, $page } = useSlideContext()
const { isPrintMode: printable } = useNav()
const active = computed(() => $nav.value.currentSlideNo === $page.value)
const host = ref<HTMLElement>()
const failed = ref(false)
let player: ReturnType<typeof AsciinemaPlayer.create> | undefined
onMounted(() => {
  if (printable.value || !host.value) return
  player = AsciinemaPlayer.create(`${import.meta.env.BASE_URL}terminal/${props.name}.cast`, host.value, {
    controls: true, autoPlay: false, preload: true, idleTimeLimit: 2,
    rows: props.short ? 12 : 20, terminalLineHeight: 1.15,
    fit: 'both', theme: 'panther', terminalFontFamily: 'Consolas, Liberation Mono, monospace',
    poster: 'npt:0:0.4',
  })
  player.addEventListener('error', () => { failed.value = true })
})
watch(active, (value) => { if (!value) player?.pause() })
onBeforeUnmount(() => player?.dispose())
</script>

<template>
  <div class="terminal-recording" :class="{ compact, short }"
       :data-recording="name">
    <img v-if="printable || failed" class="terminal-capture" :src="`${base}terminal/${name}.png`" :alt="alt" />
    <div v-else ref="host" class="recording-player" role="region" :aria-label="alt" />
  </div>
</template>

<style scoped>
.terminal-recording { height: 340px; position: relative; border: 1px solid #38516b88; border-top: 2px solid #5eead466; border-radius: 13px; background: #0b1220; }
.terminal-recording.compact { height: 315px; }
.terminal-recording.short { height: 235px; margin-top: 22px; }
.recording-player { width: 100%; height: 100%; overflow: hidden; border-radius: 12px; }
.terminal-capture { height: 100%; border: 0; }
:deep(.ap-player) {
  --term-color-background: #0b1220;
  --term-color-foreground: #e2e8f0;
  --term-color-0: #0b1220;
  --term-color-1: #fda4af;
  --term-color-2: #5eead4;
  --term-color-3: #e5c36b;
  --term-color-4: #93c5fd;
  --term-color-5: #b3a6ff;
  --term-color-6: #5eead4;
  --term-color-7: #e2e8f0;
  border-radius: 0 !important;
}
:deep(.ap-control-bar) { background: #0b1220; border-top: 1px solid #38516b88 !important; }
:deep(.ap-control-bar .ap-icon path) { fill: #5eead4; }
:deep(.ap-control-bar .ap-gutter-full) { background: #5eead4; }
:deep(.ap-timer) { color: #aec0d5; }
:deep(.ap-overlay-start) { background: transparent; }
:deep(.ap-play-button) { position: static !important; width: auto !important; height: auto !important; max-height: none !important; margin: 0 !important; }
:deep(.ap-play-button > div) { display: none; }
:deep(.ap-play-button svg) { display: none; }
:deep(.ap-play-button)::after {
  content: '▶ Reproducir ejecución';
  display: block;
  padding: 12px 20px;
  border: 1px solid #5eead466;
  border-radius: 8px;
  background: #12272b;
  color: #5eead4;
  font: 16px Arial, sans-serif;
  letter-spacing: .01em;
}
</style>
