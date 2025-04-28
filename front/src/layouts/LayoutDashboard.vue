<template>
    <div class="flex justify-between max-h-screen h-screen flex-1">
        <Leftbar />

        <div class="flex flex-col w-full">
            <Topbar />
            <div class="flex-1 rounded-lg p-4 bg-[#f2f2f2] overflow-scroll border">
                <slot />
            </div>
        </div>
        <Toaster />
    </div>
</template>

<script setup lang="ts">
import Leftbar from '@/components/baseUi/Leftbar.vue'
import Topbar from '@/components/baseUi/Topbar.vue'
import { Toaster } from 'vue-sonner'
</script>
