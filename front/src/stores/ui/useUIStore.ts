import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const isLeftbarOpen = ref(true)

  function toggleLeftbar() {
    isLeftbarOpen.value = !isLeftbarOpen.value
  }

  return {
    isLeftbarOpen,
    toggleLeftbar
  }
})
