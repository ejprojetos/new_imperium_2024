<template>
    <div class="flex justify-between h-screen">
        <Leftbar />

        <div class="flex flex-col w-full">
            <Topbar />
            <div class="flex-1 rounded-lg p-4 bg-[#f2f2f2] overflow-scroll">
                <slot />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import Leftbar from '@/components/baseUi/Leftbar.vue'
import Topbar from '@/components/baseUi/Topbar.vue'
import { useScreenSize } from '@/composables/useScreenSize'

const { isMobile } = useScreenSize()
</script>
