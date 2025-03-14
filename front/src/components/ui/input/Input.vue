<script setup lang="ts">
import type { HTMLAttributes } from 'vue'
import { cn } from '@/lib/utils'
import { useVModel } from '@vueuse/core'

const props = defineProps<{
    defaultValue?: string | number
    modelValue?: string | number
    class?: HTMLAttributes['class']
}>()

const emits = defineEmits<{
    (e: 'update:modelValue', payload: string | number): void
}>()

const modelValue = useVModel(props, 'modelValue', emits, {
    passive: true,
    defaultValue: props.defaultValue
})
</script>

<template>
    <input
        v-model="modelValue"
        :class="
            cn(
                'flex h-10 w-full rounded-full border border-gray-300 bg-background px-3 py-2 text-sm ring-offset-file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-gray-400 focus-visible:outline-hidden',
                'focus-visible:ring-2 focus-visible:ring-offset-1 disabled:cursor-not-allowed disabled:bg-gray-100 disabled:text-gray-900 transition-all text-gray-900 placeholder:font-light outline-none',
                props.class
            )
        " />
</template>
