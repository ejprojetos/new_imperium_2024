<script setup lang="ts">
import { cn } from '@/lib/utils'
import {
    ComboboxInput,
    type ComboboxInputEmits,
    type ComboboxInputProps,
    useForwardPropsEmits
} from 'reka-ui'
import { computed, type HTMLAttributes } from 'vue'

const props = defineProps<
    ComboboxInputProps & {
        class?: HTMLAttributes['class']
    }
>()

const emits = defineEmits<ComboboxInputEmits>()

const delegatedProps = computed(() => {
    const { class: _, ...delegated } = props

    return delegated
})

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
    <ComboboxInput
        v-bind="forwarded"
        :class="
            cn(
                'flex h-10 w-full rounded-full border border-gray-300 bg-background px-3 py-2 text-sm ring-offset-file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-gray-400 focus-visible:outline-hidden',
                'focus-visible:ring-2 focus-visible:ring-offset-1 disabled:cursor-not-allowed disabled:bg-gray-100 disabled:text-gray-900 transition-all text-gray-900 placeholder:font-light outline-none',
                props.class
            )
        ">
        <slot />
    </ComboboxInput>
</template>
