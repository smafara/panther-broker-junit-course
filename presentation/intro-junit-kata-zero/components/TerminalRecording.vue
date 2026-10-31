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
    fit: 'both', theme: 'dracula', terminalFontFamily: 'Consolas, Liberation Mono, monospace',
    poster: 'npt:0:1',
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
    <a v-if="!printable" class="recording-transcript" :href="`${base}terminal/${name}.cast`" download>Descargar grabación</a>
  </div>
</template>

<style scoped>
.terminal-recording { height: 340px; position: relative; border: 1px solid #526a8588; border-radius: 14px; background: #080e18; }
.terminal-recording.compact { height: 315px; }
.terminal-recording.short { height: 235px; margin-top: 22px; }
.recording-player { width: 100%; height: 100%; overflow: hidden; border-radius: 14px; }
.terminal-capture { height: 100%; border: 0; }
.recording-transcript { position: absolute; right: 6px; bottom: -20px; font-size: 11px; color: #aec0d5; }
@media print { .recording-transcript { display: none; } }
</style>
