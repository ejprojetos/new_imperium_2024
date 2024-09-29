import { ref, computed, onMounted, onUnmounted, type Ref, type ComputedRef } from 'vue'
import { useWindowSize } from '@vueuse/core'

interface ScreenSize {
  isMobile: ComputedRef<boolean>
}

export function useScreenSize(): ScreenSize {
  const { width, height } = useWindowSize()
  const isMobile: ComputedRef<boolean> = computed(() => width.value < 768)

  return { isMobile }
}
