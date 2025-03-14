// import type { Updater } from '@tanstack/vue-table'
import type { Ref } from 'vue'
import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs))
}

// export function valueUpdater<T extends Updater<any>>(updaterOrValue: T, ref: Ref) {
//     ref.value = typeof updaterOrValue === 'function' ? updaterOrValue(ref.value) : updaterOrValue
// }

export function areArraysEqual(arr1: any[] | undefined, arr2: any[]): boolean {
    if (!arr1 || !arr2) return false
    if (arr1.length !== arr2.length) return false

    return (
        arr1.every((value) => arr2.includes(value)) && arr2.every((value) => arr1.includes(value))
    )
}
