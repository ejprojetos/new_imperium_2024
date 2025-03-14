<script setup lang="ts">
import type { HTMLAttributes } from 'vue'
import { cn } from '@/lib/utils'

const props = defineProps<{
    class?: HTMLAttributes['class']
    label: string
    id: string
}>()
</script>

<template>
    <div :class="cn('flex flex-col', props.class)">
        <label class="font-medium mb-0.5" :for="props.id">{{ props.label }}</label>
        <span class="text-gray-500">
            <slot />
        </span>
    </div>
</template>
