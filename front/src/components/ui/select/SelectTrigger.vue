<script setup lang="ts">
import { cn } from '@/lib/utils'
import { ChevronDown } from 'lucide-vue-next'
import { SelectIcon, SelectTrigger, type SelectTriggerProps, useForwardProps } from 'reka-ui'
import { computed, type HTMLAttributes } from 'vue'

const props = defineProps<SelectTriggerProps & { class?: HTMLAttributes['class'] }>()

const delegatedProps = computed(() => {
    const { class: _, ...delegated } = props

    return delegated
})

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
    <SelectTrigger
        v-bind="forwardedProps"
        :class="
            cn(
                'flex h-10 w-full items-center justify-between border bg-white px-3 py-2 text-sm ring-offset-white data-[placeholder]:text-gray-400 focus:outline-none disabled:cursor-not-allowed [&>span]:truncate text-start',
                'border-gray-300 rounded-full text-gray-900 focus-visible:ring-2 focus-visible:ring-offset-1 ring-offset-primary disabled:cursor-not-allowed disabled:bg-gray-100',
                props.class
            )
        ">
        <slot />
        <SelectIcon as-child>
            <ChevronDown class="w-4 h-4 opacity-50 shrink-0" />
        </SelectIcon>
    </SelectTrigger>
</template>
