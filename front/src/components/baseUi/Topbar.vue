<template>
    <!-- Desktop -->
    <div v-if="!isMobile" class="flex items-center justify-end h-12 px-4 bg-white">
        <p class="font-bold">Olá, {{ role }}</p>
    </div>

    <!-- Mobile -->
    <div
        v-else
        class="flex items-center justify-between h-12 px-4 bg-white border-b border-gray-200"
    >
        <div class="flex items-center gap-x-4">
            <Menu @click="toggleLeftbar" />
            <p class="font-bold">Olá, {{ role }}</p>
        </div>
        topbar mobile
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { ref } from 'vue'
import { useScreenSize } from '@/composables/useScreenSize'
import { Menu } from 'lucide-vue-next'
import { useUIStore } from '@/stores/ui/useUIStore'

const { isMobile } = useScreenSize()
const { toggleLeftbar } = useUIStore()

//const { user } = storeToRefs(useUserStore());
const role = ref('Administrador')
</script>
