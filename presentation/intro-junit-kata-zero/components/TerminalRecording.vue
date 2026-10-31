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
const playing = ref(false)
let player: ReturnType<typeof AsciinemaPlayer.create> | undefined
async function togglePlayback() {
  if (!player) return
  if (playing.value) await player.pause()
  else {
    const duration = player.getDuration()
    if (duration !== undefined && player.getCurrentTime() >= duration) await player.seek(0)
    await player.play()
  }
}
onMounted(() => {
  if (printable.value || !host.value) return
  player = AsciinemaPlayer.create(`${import.meta.env.BASE_URL}terminal/${props.name}.cast`, host.value, {
    controls: false, autoPlay: false, preload: true, idleTimeLimit: 2,
    rows: props.short ? 12 : 20, terminalLineHeight: 1.15,
    fit: 'both', theme: 'panther', terminalFontFamily: 'Consolas, Liberation Mono, monospace',
    poster: 'npt:0:0.4',
  })
  player.addEventListener('error', () => { failed.value = true })
  player.addEventListener('playing', () => { playing.value = true })
  player.addEventListener('pause', () => { playing.value = false })
  player.addEventListener('ended', () => { playing.value = false })
})
watch(active, (value) => { if (!value) player?.pause() })
onBeforeUnmount(() => player?.dispose())
</script>

<template>
  <div class="terminal-recording" :class="{ compact, short }"
       :data-recording="name" :data-playing="playing">
    <img v-if="printable || failed" class="terminal-capture" :src="`${base}terminal/${name}.png`" :alt="alt" />
    <div v-else ref="host" class="recording-player" role="region" :aria-label="alt" />
    <button v-if="!printable && !failed" class="recording-toggle" type="button"
            :aria-label="playing ? 'Pausar ejecución' : 'Reproducir ejecución'"
            @click.stop="togglePlayback" />
  </div>
</template>

<style scoped>
.terminal-recording { height: 340px; position: relative; border: 1px solid #38516b88; border-top: 2px solid #5eead466; border-radius: 13px; background: #0b1220; }
.terminal-recording.compact { height: 315px; }
.terminal-recording.short { height: 235px; margin-top: 22px; }
.recording-player { width: 100%; height: 100%; overflow: hidden; border-radius: 12px; }
.terminal-capture { height: 100%; border: 0; }
.recording-toggle { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; padding: 0; background: transparent; cursor: pointer; border-radius: 12px; }
.recording-toggle:focus-visible { outline: 2px solid #5eead4; outline-offset: 3px; }
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
:deep(.ap-control-bar), :deep(.ap-overlay-start) { display: none !important; }
</style>
