<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-[50px] font-normal">Cadastrar Paciente</h1>
            <div class="pb-[70px] pt-[40px] px-[60px] mb-4 bg-white ded-lgroun gap-x-4 w-[650px]">
                <form @submit.prevent="submitForm">
                    <h2 class="mb-4 text-xl font-montserrat text-black font-bold">Identificação do paciente:</h2>
                    
                    <div class="grid grid-cols-1 gap-4">
                        <div>
                            <label class="block mb-2 text-lg font-montserrat labelText">
                                Nome completo:
                            </label>
                            <input 
                            v-model="FormData.fullName"
                            type="text"
                            class="w-full px-2 py-1 border rounded-2xl"
                            />
                        </div>
                        <div class="flex gap-[80px]">
                            <div>
                                <label class="block mb-2 text-lg font-montserrat br-16">
                                    Data de Nascimento:
                                </label>
                                <input 
                                v-model="FormData.dateOfBirth"
                                type="date"
                                class="w-[164px] px-2 py-1 border rounded-2xl"
                                />
                            </div>
                            <div>
                                <label class="block mb-2 text-lg font-montserrat br-16">
                                    Gênero:
                                </label>
                                <select 
                                v-model="FormData.gener"
                                class="w-[164px] px-2 py-1 border rounded-2xl"
                                >
                                    <option value="Feminino">Feminino</option>
                                    <option value="Masculino">Masculino</option>
                                </select>
                            </div>
                        </div>
                        <div>
                            <label class="block mb-2 text-lg font-montserrat br-16">
                                CPF:
                            </label>
                            <input 
                            v-model="FormData.cpf"
                            type="text"
                            class="w-full px-2 py-1 border rounded-2xl"
                            placeholder="999.999.999-99"
                            />
                        </div>
                    </div>
                    <h2 class="mb-4 text-xl font-montserrat text-black mt-[30px] font-bold">Endereço:</h2>
                    <div class="flex gap-[40px]">
                        <div>
                            <label class="block mb-2 text-lg font-montserrat br-16">
                                País:
                            </label>
                            <select 
                            v-model="FormData.country"
                            class="w-[100px] px-2 py-1 border rounded-2xl"
                            >
                                <option value="brasil">Brasil</option>
                                <option value="EUA">EUA</option>
                            </select>
                        </div>
                        <div>
                            <label class="block mb-2 text-lg font-montserrat br-16">
                                Estado:
                            </label>
                            <select 
                            v-model="FormData.state"
                            class="w-[100px] px-2 py-1 border rounded-2xl"
                            >
                                <option value="RN">RN</option>
                                <option value="PB">PB</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex gap-[10px] mt-3">
                        <div>
                            <label class="block mb-2 text-lg font-montserrat br-16">
                                Cidade:
                            </label>
                            <input 
                            v-model="FormData.city"
                            type="text"
                            class="w-full px-2 py-1 border rounded-2xl"
                            placeholder="Parnamirim"
                            />
                        </div>
                        <div>
                            <label class="block mb-2 text-lg font-montserrat br-16">
                                Bairro:
                            </label>
                            <input 
                            v-model="FormData.neighborhood"
                            type="text"
                            class="w-full px-2 py-1 border rounded-2xl"
                            placeholder="Nova Parnamirim"
                            />
                        </div>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16">
                            CEP:
                        </label>
                        <input 
                        v-model="FormData.zipCode"
                        type="text"
                        class="w-260 px-2 py-1 border rounded-2xl"
                        placeholder="00000-000"
                        />
                    </div>
                    <div class="flex gap-[10px]">
                        <div>
                            <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16">
                                Logradouro:
                            </label>
                            <input 
                            v-model="FormData.street"
                            type="text"
                            class="w-[432px] px-2 py-1 border rounded-2xl"
                            placeholder="Av. Maria Lacerda Montenegro"
                            />
                        </div>
                        <div>
                            <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16">
                                Número:
                            </label>
                            <input 
                            v-model="FormData.number"
                            type="text"
                            class="w-[88px] px-2 py-1 border rounded-2xl"
                            placeholder="000"
                            />
                        </div>
                    </div>
                    <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">Contato</h2>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16">
                            Email:
                        </label>
                        <input 
                        v-model="FormData.email"
                        type="email"
                        class="w-[432px] px-2 py-1 border rounded-2xl"
                        placeholder="exemplo99@email.com"
                        />
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat br-16">
                            Celular:
                        </label>
                        <input 
                        v-model="FormData.phone"
                        type="tel"
                        class="w-[250px] px-2 py-1 border rounded-2xl"
                        placeholder="(00) 0 0000-0000"
                        />
                    </div>
                    <button class="mt-[40px] bg-[#00428F] text-white w-[104px] h-[42px] rounded-lg btn"  @click="submitForm" onclick="my_modal_4.showModal() ">Cadastrar</button>
                    <dialog id="my_modal_4" class="modal" ref="modal" @click.self="closeModal">
                    <div class="modal-box w-[750px] max-w-5xl">
                        <ModalCadastro :FormData="FormData">
                            <template v-slot:header>
                                <h1 class="mb-6 font-bold text-[30px] w-[640px] text-h1 font-montserrat">Paciente cadastrado com sucesso!</h1>

                                <h2 class="mb-4 text-xl font-montserrat text-black font-bold">Identificação do paciente:</h2>
                            </template>

                        </ModalCadastro>
                        <div class="modal-action">
                            
                            <div class="flex w-full pl-[50px]">
                                <form method="dialog">
                                    <!-- if there is a button, it will close the modal -->
                                    <button  @click="closeModal" class="btn-close w-[104px] h-[42px] bg-[#DEECFA] text-white btn text-[18px]" style="color: #00428F;">Fechar</button>
                                </form>
                                <form method="dialog" class="modal-backdrop">
                                    <button>Fechar</button>
                                </form>
                                <button class="w-[180px] bg-[#00428f] text-white rounded-xl">
                                    Cadastrar Consulta
                                </button>
                            </div>
                        </div>
                    </div>
                    </dialog>
                </form>
            </div>
            
        </div>
        
    </LayoutDashboard>
</template>
   

<script setup lang="ts">
import DaysSelector from '@/components/baseUi/DaysSelector.vue';
import ModalCadastro from '@/components/baseUi/ModalCadastro.vue';
import WorkShifts from '@/components/baseUi/WorkShifts.vue';
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { reactive, ref } from 'vue';
import { toast } from 'vue-sonner';

const weekDays = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];

const shifts = ['Matutino','Vespertino','Noturno']

const selectedDays = ref<string[]>([]);

const selectedShifts = ref<string[]>([]);

//lista de dias
const handleSelectedDays = (days: string[]) =>{
    selectedDays.value = days;
}
//Lista de horários 
const handleSelectedShifts = (shifts: string[]) =>{
    selectedShifts.value = shifts;
}

// reactive pq formData é um objeto
const FormData = reactive({
    fullName: '',
    dateOfBirth: '',
    gener: 'Feminino',
    cpf: '',
    country: 'Brasil',
    state: 'RN',
    city: '',
    neighborhood: '',
    zipCode: '',
    street: '',
    number: '',
    email: '',
    phone: '',
    days:'',
    shifts:'',
    plantoes:''
})


//Constante para manipular modal e poder fechar ao clicar fora do modal
const modal = ref<HTMLDialogElement | null> (null);

//função para fechar ao clicar fora
const closeModal = () =>{
    modal.value?.close();
}

const submitForm = () => {
    
    console.log('Form submitted', FormData)
    toast.success('Salvo com sucesso!')

};



</script>


<style scoped>
    .custom-radio-square {
    /* Oculta o círculo padrão */
        appearance: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        
        /* Estilos para o quadrado */
        width: 1rem; /* Tamanho do quadrado */
        height: 1rem;
        border: 2px solid #00428F; /* Bordas do quadrado */
        background-color: transparent;
        border-radius: 4px; /* Para manter o quadrado */

        /* Efeito ao ser selecionado */
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .custom-radio-square:checked {
        background-color: #00428F; /* Cor de fundo quando selecionado */
        border-color: #00428F; /* Cor da borda quando selecionado */
    }
    h1, h2, p, span, label{
        font-family: 'montserrat';
    }
    label{
        color: #010424;
    }

</style>