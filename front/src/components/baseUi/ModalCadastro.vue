<template>
    <div class="pb-[70px] pt-[40px] px-[60px] mb-4 bg-white ded-lgroun gap-x-4 w-[650px] rounded-xl">

        <header>
            <slot name="header" class="mb-6 text-4xl font-bold text-3xl">Cadastrado com sucesso!</slot>
        </header>
        
    
        <div class="flex flex-col">
            <label class="block mt-[10px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                Nome completo:
            </label>
            <p>
                {{ `${props.FormData.name} ${props.FormData.lastName}` }}
            </p>
        </div>
        <div class="flex gap-[80px]">
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
                    Data de Nascimento:
                </label>
                <p>
                    {{ formatDate(props.FormData.dateOfBirth)}}
                </p>
            </div>
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
                    Gênero:
                </label>
                <p>
                    {{ props.FormData.gener }}
                </p>
            </div>
        </div>
        <div>
            <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                CPF:
            </label>
            <p>
                {{props.FormData.cpf}}
            </p>
        </div>
        <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">Endereço:</h2>
        <div class="flex gap-[90px]" >
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                País:
                </label>
                <p>
                    {{props.FormData.country}}
                </p>
            </div>
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                Estado:
                </label>
                <p>
                    {{props.FormData.state}}
                </p>
            </div>
        </div>
        <div class="flex gap-[173px]" >
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                    Cidade:
                </label>
                <p>
                    {{props.FormData.city}}
                </p>
            </div>
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                    Bairro:
                </label>
                <p>
                    {{props.FormData.neighborhood}}
                </p>
            </div>
        </div>
        <div>
            <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                    CEP:
                </label>
                <p>
                    {{props.FormData.zipCode}}
                </p>
        </div>
        <div class="flex gap-[165px]">
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                    Logradouro:
                </label>
                <p>
                    {{props.FormData.street}}
                </p>
            </div>
            <div>
                <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                    Número:
                </label>
                <p>
                    {{props.FormData.number}}
                </p>
            </div>
        </div>
        <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">Contato:</h2>
        <div>
            <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                Email:
            </label>
            <p>
                {{props.FormData.email}}
            </p>
        </div>
        <div>
            <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold" >
                Celular:
            </label>
            <p>
                {{props.FormData.phone}}
            </p>
        </div>
     
    






        <slot/>
    </div>
</template>

<script setup lang="ts">
import {defineProps } from 'vue';

interface formData{
    name: string;
    lastName: string;
    dateOfBirth: string;
    gener: string;
    cpf: string;
    country: string;
    state: string;
    city: string;
    neighborhood: string;
    zipCode: string;
    street: string;
    number: string;
    email: string;
    phone: string;
    days: string[];
}

const props = defineProps<{
    FormData: formData;
}>();

const formatDate = (date: string) =>{
    const [year, month, day] = date.split('-')
    const d = new Date(Number(year), Number(month), Number(day));
    return d.toLocaleDateString('pt-BR');
}

</script>

<style>
    label{
        font-size: 1.25rem;
    }
    p{
        font-family: 'Montserrat';
        font-size: 1.125rem;
    }
</style>