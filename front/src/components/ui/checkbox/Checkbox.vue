<script setup lang="ts">
import type { CheckboxRootEmits, CheckboxRootProps } from 'reka-ui'
import { cn } from '@/lib/utils'
import { CheckboxIndicator, CheckboxRoot, useForwardPropsEmits } from 'reka-ui'
import { computed, type HTMLAttributes } from 'vue'

const props = defineProps<CheckboxRootProps & { class?: HTMLAttributes['class']; label: string }>()
const emits = defineEmits<CheckboxRootEmits>()

const delegatedProps = computed(() => {
    const { class: _, ...delegated } = props

    return delegated
})

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
    <CheckboxRoot
        v-bind="forwarded"
        :class="
            cn(
                'peer relative shrink-0 bg-blue-200 text-primary flex rounded-full px-3 py-1 border border-primary text-sm font-medium transition-colors duration-300 ease-in-out ring-offset-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-300 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-60 data-[state=checked]:bg-primary data-[state=checked]:text-gray-50',
                props.class
            )
        ">
        <CheckboxIndicator
            class="absolute flex h-full w-full items-center justify-center text-current"></CheckboxIndicator>
        {{ props.label }}
    </CheckboxRoot>
</template>
