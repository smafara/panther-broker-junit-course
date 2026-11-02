<script setup lang="ts">
defineProps<{ file: string }>()
const base = import.meta.env.BASE_URL
</script>

<template>
  <img :src="`${base}logos/${file}`" />
</template>
