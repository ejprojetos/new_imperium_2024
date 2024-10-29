<template>
    <div class="flex flex-wrap gap-x-[10px] gap-y-[15px]">
        <span
        v-for="(day, index) in days"
        :key="index"
        @click="() => toggleDay(day)"
        :class="[
        'cursor-pointer px-4 py-2 rounded-2xl w-[90px] h-[30px] flex items-center justify-center font-montserrat',
        selectedDays.includes(day) ? 'bg-[#00428F] text-white' : 'bg-[#DEECFA] text-gray-700'
      ]"
        >{{ day }}</span>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'; 

const selectedDays = ref<string[]>([])

//emitir evento
const emit = defineEmits(['update:selectedDays']);

//Armazenar os dias selecionados
const days = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']


//Função para alternar a seleção dos dias
const toggleDay = (day: string) => {
    if(selectedDays.value.includes(day)){
        selectedDays.value = selectedDays.value.filter(selectedDay => selectedDay !== day);
    } else{
        selectedDays.value.push(day)
    }

    //emite o array para o component pai
    emit('update:selectedDays', selectedDays.value)
}

</script>

<style scoped>
    button {
    transition: background-color 0.3s, color 0.3s;
    }

    
</style>