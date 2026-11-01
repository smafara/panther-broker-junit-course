<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'
import * as AsciinemaPlayer from 'asciinema-player'
import 'asciinema-player/dist/bundle/asciinema-player.css'
import verifiedResults from '../data/test-results.json'

const props = defineProps<{ name: string, alt: string, compact?: boolean, short?: boolean, revealAt?: number }>()
const base = import.meta.env.BASE_URL
const { $nav, $page, $clicks } = useSlideContext()
const { isPrintMode: printable } = useNav()
const active = computed(() => $nav.value.currentSlideNo === $page.value)
const visible = computed(() => active.value && $clicks.value >= (props.revealAt ?? 0))
const tests = computed(() => (verifiedResults as Record<string, {name: string, status: string}[]>)[props.name] ?? [])
const revealed = ref(0)
const completed = ref(false)
const shownCount = computed(() => printable.value ? tests.value.length : revealed.value)
const passedCount = computed(() => tests.value.slice(0, shownCount.value).filter(test => test.status === 'passed').length)
const host = ref<HTMLElement>()
const failed = ref(false)
const playing = ref(false)
let player: ReturnType<typeof AsciinemaPlayer.create> | undefined
let startTimer: ReturnType<typeof setTimeout> | undefined
const resultTimers: ReturnType<typeof setTimeout>[] = []
function clearTimers() {
  clearTimeout(startTimer)
  resultTimers.splice(0).forEach(clearTimeout)
}
function resetResults() { revealed.value = 0; completed.value = false }
async function startFromBeginning() {
  resetResults()
  await player?.seek(0)
  if (visible.value) await player?.play()
}
async function togglePlayback() {
  clearTimeout(startTimer)
  if (!player) return
  if (playing.value) await player.pause()
  else {
    const duration = player.getDuration()
    if (completed.value || (duration !== undefined && player.getCurrentTime() >= duration)) {
      clearTimers()
      resetResults()
      await player.seek(0)
    }
    await player.play()
  }
}
onMounted(() => {
  if (printable.value || !host.value) return
  player = AsciinemaPlayer.create(`${import.meta.env.BASE_URL}terminal/${props.name}.cast`, host.value, {
    controls: false, autoPlay: false, preload: true, idleTimeLimit: 2, speed: 0.75,
    rows: props.short ? 8 : (tests.value.length ? 12 : 20), terminalLineHeight: 1.15,
    fit: 'both', theme: 'panther', terminalFontFamily: 'Consolas, Liberation Mono, monospace',
    poster: 'npt:0:0.4',
  })
  player.addEventListener('error', () => { failed.value = true })
  player.addEventListener('playing', () => { playing.value = true })
  player.addEventListener('pause', () => { playing.value = false })
  player.addEventListener('ended', () => {
    playing.value = false
    completed.value = true
    // Present the verified XML outcomes after playback, in teaching order.
    tests.value.forEach((_, index) => resultTimers.push(setTimeout(() => {
      if (visible.value) revealed.value = index + 1
    }, 350 + index * 450)))
  })
  if (visible.value) startTimer = setTimeout(startFromBeginning, 500)
})
watch(visible, (value) => {
  clearTimers()
  if (!value) player?.pause()
  else if (player) startTimer = setTimeout(startFromBeginning, 500)
})
onBeforeUnmount(() => { clearTimers(); player?.dispose() })
</script>

<template>
  <div class="terminal-recording" :class="{ compact, short, 'has-results': tests.length, 'is-visible': printable || visible }"
       :data-recording="name" :data-playing="playing" data-speed="0.75" :data-completed="completed">
    <div class="recording-screen">
      <img v-if="printable || failed" class="terminal-capture" :src="`${base}terminal/${name}.png`" :alt="alt" />
      <div v-else ref="host" class="recording-player" role="region" :aria-label="alt" />
      <button v-if="!printable && !failed" class="recording-toggle" type="button"
            :aria-label="playing ? 'Pausar ejecución' : 'Reproducir ejecución'"
            @click.stop="togglePlayback" />
    </div>
    <div v-if="tests.length" class="test-results" role="status" aria-live="polite" aria-label="Resultados de las pruebas">
      <div class="results-header"><span>PRUEBAS</span><span>{{ shownCount ? `${passedCount} de ${tests.length} correctas` : 'En ejecución' }}</span></div>
      <div v-for="(test, index) in tests" :key="test.name" class="test-result"
           :class="index < shownCount ? test.status : 'pending'" :data-test-name="test.name"
           :data-status="index < shownCount ? test.status : 'pending'">
        <span class="result-icon">{{ index < shownCount ? (test.status === 'passed' ? '✓' : '×') : '○' }}</span>
        <span class="result-name">{{ test.name }}()</span>
        <span class="result-status">{{ index < shownCount ? (test.status === 'passed' ? 'Correcta' : 'Falló') : 'Pendiente' }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.terminal-recording { height: 340px; position: relative; border: 1px solid #38516b88; border-top: 2px solid #5eead466; border-radius: 13px; background: #0b1220; opacity: 0; }
.terminal-recording.is-visible { opacity: 1; animation: terminal-reveal .5s ease both; }
@keyframes terminal-reveal { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.terminal-recording.compact { height: 315px; }
.terminal-recording.short { height: 235px; margin-top: 22px; }
.terminal-recording.short.has-results { height: 270px; }
.recording-screen { height: 100%; position: relative; }
.has-results .recording-screen { height: calc(100% - 108px); }
.recording-player { width: 100%; height: 100%; overflow: hidden; border-radius: 12px; }
.terminal-capture { height: 100%; border: 0; }
.recording-toggle { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; padding: 0; background: transparent; cursor: pointer; border-radius: 12px; }
.recording-toggle:focus-visible { outline: 2px solid #5eead4; outline-offset: 3px; }
.test-results { height: 108px; box-sizing: border-box; border-top: 1px solid #38516b88; padding: 7px 14px; }
.results-header { display: flex; justify-content: space-between; font: 11px Arial, sans-serif; letter-spacing: .08em; color: #aec0d5; margin-bottom: 5px; }
.test-result { display: flex; align-items: center; gap: 9px; min-height: 24px; border-radius: 4px; padding: 0 7px; color: #91a6bf; transition: color .35s, background .35s; font: 14px Consolas, 'Liberation Mono', monospace; }
.test-result.passed { color: #5eead4; background: #5eead410; }
.test-result.failed { color: #fda4af; background: #fda4af15; }
.result-name { flex: 1; }
.result-icon { font-size: 16px; width: 16px; }
.result-status { font: 12px Arial, sans-serif; }
@media (prefers-reduced-motion: reduce) { .terminal-recording.is-visible { animation: none; } }
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
