<template>
    <div class="flex flex-wrap gap-x-[10px] gap-y-[15px]">
        <button
        v-for="(shift, index) in shifts"
        :key="index"
        @click="() => toggleShift(shift)"
        :class="[
        'px-4 py-2 rounded-2xl cursor-pointer w-[90px] h-[30px] flex items-center justify-center font-montserrat',
        selectedShifts.includes(shift) ? 'bg-[#00428F] text-white' : 'bg-[#DEECFA] text-gray-700'
      ]"
        >{{ shift }}</button>
    
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const selectedShifts = ref<string[]>([])

// Emitir evento
const emit = defineEmits(['update:selected-shifts'])

const shifts = ['Matutino', 'Vespertino', 'Noturno']

//função para alternar a seleção dos turno

const toggleShift = (shift: string) => {
    if(selectedShifts.value.includes(shift)){
        selectedShifts.value = selectedShifts.value.filter(selectedShift => selectedShift !== shift);
    }else{
        selectedShifts.value.push(shift)
    }

    emit('update:selected-shifts', selectedShifts.value)
}
</script>

<style scoped>

</style>