import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
    const isLeftbarOpen = ref(false)
    const isMobile = ref(false)

    function toggleLeftbar() {
        isLeftbarOpen.value = !isLeftbarOpen.value
    }

    function setMobile(value: boolean) {
        isMobile.value = value
        if (value) {
            isLeftbarOpen.value = false
        }
    }

    return {
        isLeftbarOpen,
        isMobile,
        toggleLeftbar,
        setMobile
    }
})
