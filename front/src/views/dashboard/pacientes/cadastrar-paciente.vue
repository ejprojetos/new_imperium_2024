<template>
    <LayoutDashboard>
        <div class="sm:ml-[60px] mt-[29px]">
            <router-link to="/dashboard/medicos">
                <h2
                    class="text-lg font-semibold text-gray-600 transition duration-300 ease-in-out sm:text-xl hover:text-gray-800">
                    < Voltar
                </h2>
            </router-link>
        </div>

        <div class="grid grid-cols-1 gap-4 ml-[25px] sm:ml-[145px] mt-[20px]">
            <h1 class="mb-6 text-[1.75rem] font-normal sm:text-[3.125rem] sm:font-montserrat">
                Cadastrar Paciente
            </h1>
            <div
                class="rounded-xl sm:rounded-none pb-[70px] pt-[29px] sm:pt-[40px] px-[20px] sm:px-[60px] mb-4 bg-white ded-lgroun gap-x-4 sm:w-[650px]"
                style="
                    box-shadow: 0px 4px 4px 0px #00000040;
                    box-shadow: 0px 4px 4px 0px #00000040;
                    box-shadow: 0px -2px 0px 0px #00000040;
                ">
                <form @submit.prevent="submitForm">
                    <h2 class="mb-4 text-xl font-bold text-black font-montserrat">
                        Identificação do paciente:
                    </h2>

                    <div class="grid grid-cols-1 gap-4">
                        <div>
                            <label class="block mb-2 text-sm sm:text-lg font-montserrat">
                                Nome completo:
                            </label>
                            <input
                                v-model="FormData.fullName"
                                type="text"
                                class="px-2 py-1 w-full rounded-2xl border" />
                            <div v-if="formErrors.fullName" class="mt-1 text-sm text-red-500">
                                {{ formErrors.fullName }}
                            </div>
                        </div>
                        <div class="sm:flex flex-coll gap-[80px]">
                            <div>
                                <label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
                                    Data de Nascimento:
                                </label>
                                <input
                                    v-model="FormData.dateOfBirth"
                                    type="date"
                                    class="w-[164px] px-2 py-1 border rounded-2xl" />
                                <div
                                    v-if="formErrors.dateOfBirth"
                                    class="mt-1 text-sm text-red-500">
                                    {{ formErrors.dateOfBirth }}
                                </div>
                            </div>
                            <div>
                                <label
                                    class="mt-[20px] sm:mt-0 block mb-2 text-sm sm:text-lg font-montserrat br-16">
                                    Gênero:
                                </label>
                                <select
                                    v-model="FormData.gener"
                                    class="w-[164px] px-2 py-1 border rounded-2xl">
                                    <option value="Feminino">Feminino</option>
                                    <option value="Masculino">Masculino</option>
                                </select>
                                <div v-if="formErrors.gener" class="mt-1 text-sm text-red-500">
                                    {{ formErrors.gener }}
                                </div>
                            </div>
                        </div>
                        <div>
                            <label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
                                CPF:
                            </label>
                            <input
                                v-model="FormData.cpf"
                                type="text"
                                class="px-2 py-1 w-full rounded-2xl border"
                                placeholder="999.999.999-99" />
                            <div v-if="formErrors.cpf" class="mt-1 text-sm text-red-500">
                                {{ formErrors.cpf }}
                            </div>
                        </div>
                    </div>
                    <h2 class="mb-4 text-xl font-montserrat text-black mt-[30px] font-bold">
                        Endereço:
                    </h2>
                    <div class="flex gap-[40px]">
                        <div>
                            <label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
                                País:
                            </label>
                            <select
                                v-model="FormData.country"
                                class="w-[100px] px-2 py-1 border rounded-2xl">
                                <option value="brasil">Brasil</option>
                                <option value="EUA">EUA</option>
                            </select>
                        </div>
                        <div>
                            <label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
                                Estado:
                            </label>
                            <select
                                v-model="FormData.state"
                                class="w-[100px] px-2 py-1 border rounded-2xl">
                                <option value="RN">RN</option>
                                <option value="PB">PB</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex-coll sm:flex gap-[10px] mt-3">
                        <div>
                            <label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
                                Cidade:
                            </label>
                            <input
                                v-model="FormData.city"
                                type="text"
                                class="px-2 py-1 w-full rounded-2xl border"
                                placeholder="Parnamirim" />
                        </div>
                        <div>
                            <label
                                class="mt-[20px] sm:mt-0 block mb-2 text-sm sm:text-lg font-montserrat br-16">
                                Bairro:
                            </label>
                            <input
                                v-model="FormData.neighborhood"
                                type="text"
                                class="px-2 py-1 w-full rounded-2xl border"
                                placeholder="Nova Parnamirim" />
                        </div>
                    </div>
                    <div>
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            CEP:
                        </label>
                        <input
                            v-model="FormData.zipCode"
                            type="text"
                            class="px-2 py-1 rounded-2xl border w-260"
                            placeholder="00000-000" />
                    </div>
                    <div class="flex-coll sm:flex gap-[10px]">
                        <div>
                            <label
                                class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                                Logradouro:
                            </label>
                            <input
                                v-model="FormData.street"
                                type="text"
                                class="w-full sm:w-[432px] px-2 py-1 border rounded-2xl"
                                placeholder="Av. Maria Lacerda Montenegro" />
                        </div>
                        <div>
                            <label
                                class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                                Número:
                            </label>
                            <input
                                v-model="FormData.number"
                                type="text"
                                class="w-[88px] px-2 py-1 border rounded-2xl"
                                placeholder="000" />
                        </div>
                    </div>
                    <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">
                        Contato
                    </h2>
                    <div>
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            Email:
                        </label>
                        <input
                            v-model="FormData.email"
                            type="email"
                            class="w-full sm:w-[432px] px-2 py-1 border rounded-2xl"
                            placeholder="exemplo99@email.com" />
                        <div v-if="formErrors.email" class="mt-1 text-sm text-red-500">
                            {{ formErrors.email }}
                        </div>
                    </div>
                    <div>
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            Celular:
                        </label>
                        <input
                            v-model="FormData.phone"
                            type="tel"
                            class="w-[250px] px-2 py-1 border rounded-2xl"
                            placeholder="(00) 0 0000-0000" />
                        <div v-if="formErrors.phone" class="mt-1 text-sm text-red-500">
                            {{ formErrors.phone }}
                        </div>
                    </div>
                    <!-- <button
                        class="mt-[40px] bg-[#00428F] text-white w-[104px] h-[42px] rounded-lg btn"
                        @click="submitForm"
                        onclick="my_modal_4.showModal() ">
                        Cadastrar
                    </button> -->

                    <!-- modal removido para evitar mais complexidade -->
                    <button
                        class="mt-[40px] bg-[#00428F] text-white w-[104px] h-[42px] rounded-lg btn"
                        @click="submitForm">
                        Cadastrar
                    </button>

                    <dialog id="my_modal_4" class="modal" ref="modal" @click.self="closeModal">
                        <div class="modal-box w-[310px] sm:w-[750px] max-w-5xl">
                            <div>
                                <h1
                                    class="font-montserrat text-[1.375rem] font-semibold text-center">
                                    Paciente cadastrado com sucesso!
                                </h1>
                            </div>

                            <ModalCadastro :FormData="FormData">
                                <template v-slot:header>
                                    <h1
                                        class="mb-6 font-bold text-[30px] w-[640px] text-h1 font-montserrat">
                                        Paciente cadastrado com sucesso!
                                    </h1>

                                    <h2 class="mb-4 text-xl font-bold text-black font-montserrat">
                                        Identificação do paciente:
                                    </h2>
                                </template>
                            </ModalCadastro>
                            <div class="modal-action">
                                <div class="flex w-full pl-[50px] justify-center sm:justify-start">
                                    <form method="dialog">
                                        <!-- if there is a button, it will close the modal -->
                                        <button
                                            @click="closeModal"
                                            class="btn-close w-[104px] h-[42px] bg-[#00428f] sm:bg-[#DEECFA] text-white sm:text-[#00428f] btn text-[18px] text-white">
                                            Fechar
                                        </button>
                                    </form>
                                    <form method="dialog" class="modal-backdrop">
                                        <button>Fechar</button>
                                    </form>
                                    <button
                                        class="hidden sm:block w-[180px] bg-[#00428f] text-white rounded-xl">
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
import ModalCadastro from '@/components/baseUi/ModalCadastro.vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { reactive, ref } from 'vue'
import { toast } from 'vue-sonner'
import { useUserStore } from '@/stores/users/users.store'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()
// dados do formulário
const FormData = ref({
    fullName: '',
    dateOfBirth: '',
    gener: '',
    cpf: '',
    country: '',
    state: '',
    city: '',
    neighborhood: '',
    zipCode: '',
    street: '',
    number: '',
    email: '',
    phone: ''
})

// adiciona refs para controle de validação
const formErrors = ref<Record<string, string>>({})

const modal = ref<HTMLDialogElement | null>(null)

// função para fechar ao clicar fora
const closeModal = () => {
    if (modal.value) {
        modal.value.close()
    }
}

// função para validar o formulário
const validateForm = () => {
    const errors: Record<string, string> = {}

    // validação do nome
    if (!FormData.value.fullName) {
        errors.fullName = 'O nome é obrigatório'
    }

    // validação do cpf
    if (!FormData.value.cpf) {
        errors.cpf = 'o cpf é obrigatório'
    } else if (!/^\d{3}\.\d{3}\.\d{3}-\d{2}$/.test(FormData.value.cpf)) {
        errors.cpf = 'CPF inválido'
    }

    // validação do email
    if (!FormData.value.email) {
        errors.email = 'o email é obrigatório'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(FormData.value.email)) {
        errors.email = 'Email inválido'
    }

    // validação da data de nascimento
    if (!FormData.value.dateOfBirth) {
        errors.dateOfBirth = 'a data de nascimento é obrigatória'
    }

    // validação do gênero
    if (!FormData.value.gener) {
        errors.gener = 'O gênero é obrigatório'
    }

    // validação do telefone
    // if (!FormData.value.phone) {
    //     errors.phone = 'o telefone é obrigatório'
    // } else if (!/^\(\d{2}\) \d \d{4}-\d{4}$/.test(FormData.value.phone)) {
    //     errors.phone = 'telefone inválido'
    // }

    formErrors.value = errors
    return Object.keys(errors).length === 0
}

// função para enviar o formulário
const submitForm = async () => {
    try {
        // valida o formulário antes de enviar
        if (!validateForm()) {
            toast.error('por favor, preencha todos os campos obrigatórios')
            return
        }

        // prepara os dados para envio
        const patientData = {
            first_name: FormData.value.fullName.split(' ')[0],
            last_name: FormData.value.fullName.split(' ').slice(1).join(' '),
            email: FormData.value.email,
            cpf: FormData.value.cpf,
            date_birth: FormData.value.dateOfBirth,
            gender: FormData.value.gener,
            role: 'PATIENT',
            address: {
                country: FormData.value.country,
                state: FormData.value.state,
                city: FormData.value.city,
                neighborhood: FormData.value.neighborhood,
                street: FormData.value.street,
                number: FormData.value.number,
                zipcode: FormData.value.zipCode
            },
            phone: FormData.value.phone
        }

        // envia os dados para a api
        // await userService.createDoctor(patientData)
        let response = await userStore.createDoctor(patientData)
        console.log(response)

        // mostra mensagem de sucesso
        toast.success('paciente cadastrado com sucesso!')

        // mostra o modal de sucesso
        if (modal.value) {
            modal.value.showModal()
        }

        // redireciona para a lista de pacientes após 2 segundos
        setTimeout(() => {
            router.push('/dashboard/pacientes')
        }, 2000)
    } catch (error: any) {
        console.error('erro:', error)
        if (error.errors) {
            // atualiza os erros de validação
            formErrors.value = Object.keys(error.errors).reduce(
                (acc: Record<string, string>, key: string) => {
                    acc[key] = error.errors[key][0]
                    return acc
                },
                {}
            )
        }
        toast.error('erro ao cadastrar paciente')
    }
}
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
    border: 2px solid #00428f; /* Bordas do quadrado */
    background-color: transparent;
    border-radius: 4px; /* Para manter o quadrado */

    /* Efeito ao ser selecionado */
    display: flex;
    align-items: center;
    justify-content: center;
}

.custom-radio-square:checked {
    background-color: #00428f; /* Cor de fundo quando selecionado */
    border-color: #00428f; /* Cor da borda quando selecionado */
}
h1,
h2,
p,
span,
label {
    font-family: 'montserrat';
}
label {
    color: #010424;
}
</style>
