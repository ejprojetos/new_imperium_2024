<template>
    <LayoutDashboard>
        <div class="grid grid-cols-1 gap-4 px-12 mt-12">
            <router-link to="/dashboard/medicos">
                <h2 class="text-xl font-semibold text-gray-600 hover:text-gray-800 transition duration-300 ease-in-out">
                    < Voltar</h2>
            </router-link>

            <h1 class="w-1/2 mx-auto titulo-cadastro">Cadastrar Consulta</h1>
            <div class="p-6 bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto p-10 box">

                <div class="grid grid-cols-1 gap-4">

                    <div>
                        <label for="fullName" class="block mb-1 font-semibold titulo-label">Nome do Paciente:</label>
                        <select class="select select-bordered w-full texto-opcoes" v-model="optionSelected.fullName">
                            <option v-for="option in formData.fullName" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label for="consultation" class="block mb-1 font-semibold titulo-label">Consulta:</label>
                        <select class="select select-bordered w-full texto-opcoes"
                            v-model="optionSelected.consultation">
                            <option v-for="option in formData.consultation" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label for="specialty" class="block mb-1 font-semibold titulo-label">Especialidade:</label>
                        <select class="select select-bordered w-full texto-opcoes" v-model="optionSelected.specialty">
                            <option v-for="option in formData.specialty" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label for="medicName" class="block mb-1 font-semibold titulo-label">Médico:</label>
                        <select class="select select-bordered w-full texto-opcoes" v-model="optionSelected.medicName">
                            <option v-for="option in formData.medicName" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label for="room" class="block mb-1 font-semibold titulo-label">Local:</label>
                        <select class="select select-bordered w-full texto-opcoes" v-model="optionSelected.room">
                            <option v-for="option in formData.room" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div class="grid grid-cols-1 gap-1">

                        <label class="block mb-1 font-semibold">Motivo da consulta:</label>
                        <input type="text" placeholder="Digite o motivo da consulta"
                            class="input input-bordered w-full rounded-full texto-opcoes" v-model="motivo" />

                    </div>
                    <div class="grid grid-cols-2 gap-1">

                        <div class="grid grid-cols-1 gap-1">
                            <label for="dateInput" class="block mb-1 font-semibold ">Selecione uma
                                data:</label>
                            <input type="date" id="dateInput" v-model="selectedDate" @change="handleDateChange"
                                class="input input-bordered rounded-full w-3/6 input-group" />
                        </div>
                        <div class="grid grid-cols-1 gap-1">
                            <label for="timeInput" class="block mb-1 font-semibold">Selecione uma hora:</label>
                            <input type="time" id="timeInput" v-model="selectedTime" @change="handleTimeChange"
                                class="input input-bordered rounded-full w-2/5 px-5 input-group" />
                        </div>

                    </div>
                    <div class="flex gap-x-2">

                        <label for="timeInput" class="block mb-1 font-semibold">Fila:</label>
                        <label for="">1º</label>

                    </div>
                    <button class="btn btn-active btn-neutral w-1/6 text-white p-1 hover:bg-blue"
                        style="background-color: #00428F;" onclick="my_modal_2.showModal()">Cadastrar</button>


                    <dialog id="my_modal_2" class="modal">
                        <div class="modal-box grid grid-cols-1 gap-4">

                            <h3 class="text-lg font-bold titulo-modal">Consulta cadastrada com sucesso!</h3>

                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold"> {{ labels.fullName }}:</label>
                                <label> {{ optionSelected.fullName }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold"> {{ labels.consultation }}:</label>
                                <label> {{ optionSelected.consultation }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold"> {{ labels.specialty }}:</label>
                                <label> {{ optionSelected.specialty }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold"> {{ labels.medicName }}:</label>
                                <label> {{ optionSelected.medicName }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold"> {{ labels.room }}:</label>
                                <label> {{ optionSelected.room }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold"> {{ labels.reason }}:</label>
                                <label> {{ motivo }}</label>
                            </div>
                            <div class="grid grid-cols-2">
                                <div class="grid grid-cols-1">
                                    <label for="" class="font-semibold"> {{ labels.date }}:</label>
                                    <label> {{ formattedDate }}</label>
                                </div>
                                <div class="grid grid-cols-1">
                                    <label for="" class="font-semibold"> {{ labels.time }}:</label>
                                    <label> {{ selectedTime }}</label>
                                </div>
                            </div>
                            <div class="grid grid-cols-1">

                            </div>

                            <label for="timeInput" class="block mb-1 font-semibold">Fila: 1º</label>

                            <button class="btn btn-active btn-neutral w-1/6 text-white hover:bg-blue"
                                style="background-color: #00428F;" onclick="my_modal_2.close()">Fechar</button>

                        </div>
                        <form method="dialog" class="modal-backdrop">
                            <button>close</button>
                        </form>
                    </dialog>


                </div>
            </div>
        </div>
    </LayoutDashboard>


</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { ref, reactive, computed } from 'vue'
const motivo = ref('')

const optionSelected = ref({
    fullName: 'N/D',
    consultation: 'N/D',
    specialty: 'N/D',
    medicName: 'N/D',
    room: 'N/D'
})
const formData = reactive({
    profileImage: '../../../assets/placeholder.png',
    fullName: [
        'Gabriele Rocha de Carvalho',
        'Rômulo Deyvid',
        'Han Solo',
        'Greedo'
    ],
    consultation: [
        '1ª Consulta',
        'Retorno',
    ],
    specialty: [
        'Oftalmologia',
        'Cardiologia',
        'Urologia'
    ],
    medicName: [
        'Dra. Rafaela Veríssimo',
        'Dra. Alexandre de Melo Carneiro',
        'Dr. Carlos Mendes',
    ],
    room: [
        'Sala 01',
        'Sala 02',
        'Sala 03',
    ],
    birthDate: '10/10/1981',
    gender: 'Feminino',
    cpf: '999.999.999-99',
    country: 'Brasil',
    state: 'RN',
    city: 'Parnamirim',
    neighborhood: 'Nova Parnamirim',
    zipCode: '00000-000',
    street: 'Av. Ayrton Senna',
    number: '000',
    email: 'exemplo99@hotmail.com',
    phone: '(00) 00000-0000',
    allergies: '',
    recurringProblems: '',
    medication: ''
})

const personalInfo = {
    fullName: '',
    consultation: '',
    specialty: '',
    medicName: '',
    room: ''
}



const labels = {
    fullName: 'Nome do Paciente',
    consultation: 'Consulta',
    specialty: 'Especialidade',
    medicName: 'Nome do médico',
    reason: 'Motivo da consulta',
    date: 'Data da Consulta',
    time: 'Hora da Consulta',
    room: 'Local',
    gender: 'Gênero',
    cpf: 'CPF',
    country: 'País',
    state: 'Estado',
    city: 'Cidade',
    neighborhood: 'Bairro',
    zipCode: 'CEP',
    street: 'Logradouro',
    number: 'Número',
    email: 'Email',
    phone: 'Celular'
}
const selectedDate = ref(null);

const handleDateChange = () => {
    console.log("Data selecionada:", selectedDate.value);
};

const formattedDate = computed(() => {
    if (!selectedDate.value) return '';

    // Convertendo para a data local sem alterar o dia
    const [year, month, day] = selectedDate.value.split("-");
    const localDate = new Date(year, month - 1, day);

    return localDate.toLocaleDateString();
});
const selectedTime = ref(null);

const handleTimeChange = () => {
    console.log("Hora selecionada:", selectedTime.value);
};

</script>

<style scoped>
select {
    border-radius: 50px;
    width: 100%;
}

.box {
    width: 50%;
}

.titulo-modal {
    color: #010424;
    font-family: Montserrat;
    font-size: 30px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.titulo-cadastro {
    color: #010424;
    font-family: Montserrat;
    font-size: 50px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.titulo-label {
    color: #010424;
    font-family: Montserrat;
    font-size: 20px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.texto-opcoes {
    color: #010424;
    font-family: Montserrat;
    font-size: 18px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

input::placeholder {
    color: #010424;
    font-family: Montserrat;
    font-size: 18px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

.input-group {
    height: 2rem;
}

.modal-box {
    max-width: 40rem;
}
</style>