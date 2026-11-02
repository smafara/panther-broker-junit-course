<script setup lang="ts">
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const { $nav, $page } = useSlideContext()
const { isPrintMode } = useNav()
const base = import.meta.env.BASE_URL
const active = computed(() => $nav.value.currentSlideNo === $page.value)
const rows = [
  { language: 'Java', tool: 'JUnit', logo: 'junit.svg' },
  { language: 'C++', tool: 'doctest', logo: 'doctest.svg' },
  { language: 'C# / .NET', tool: 'xUnit.net', logo: 'xunit.svg' },
  { language: 'Python', tool: 'pytest', logo: 'pytest.svg' },
  { language: 'JavaScript', tool: 'Jest', logo: 'jest.png' },
]
</script>

<template>
  <table class="testing-tools">
    <thead><tr><th>Lenguaje</th><th>Ejemplo de herramienta</th></tr></thead>
    <tbody>
      <tr v-for="(row, index) in rows" :key="row.tool"
          :class="{ 'is-active': active || isPrintMode, 'is-print': isPrintMode }"
          :style="{ '--row-delay': `${index * 400}ms` }">
        <td>{{ row.language }}</td>
        <td><span class="tool"><img :src="`${base}logos/${row.logo}`" alt="" /><span>{{ row.tool }}</span></span></td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.testing-tools tbody tr { opacity: 0; }
.testing-tools tbody tr.is-active { animation: appear .4s ease both; animation-delay: var(--row-delay); }
.testing-tools tbody tr.is-print { animation: none; opacity: 1; }
.tool { display: flex; align-items: center; gap: 16px; }
.tool img { display: block; width: 38px; height: 38px; object-fit: contain; }
@keyframes appear { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
@media (prefers-reduced-motion: reduce) {
  .testing-tools tbody tr.is-active { animation: none; opacity: 1; }
}
</style>
