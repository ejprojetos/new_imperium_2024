<template>
    <LayoutDashboard>
        <div class="sm:ml-[60px] mt-[29px]">
            <router-link to="/dashboard/medicos">
                <h2
                    class="text-lg font-semibold text-gray-600 transition duration-300 ease-in-out hover:text-gray-800 sm:text-xl">
                    < Voltar
                </h2>
            </router-link>
        </div>

        <div class="grid grid-cols-1 gap-4 ml-[25px] sm:ml-[145px] mt-[20px]">
            <h1 class="mb-6 text-[1.75rem] font-normal sm:text-[3.125rem] sm:font-montserrat">
                Cadastrar Médico
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
                        Dados Pessoais:
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
                    </div>

                    <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">
                        Dados Profissionais
                    </h2>
                    <div>
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            Formação:
                        </label>
                        <select
                            v-model="FormData.degree"
                            class="w-full sm:w-[432px] px-2 py-1 border rounded-2xl">
                            <option value="GraduaçãoCompleta">
                                Graduação e Pós-Graduação completo
                            </option>
                            <option value="Mestrado">Mestrado Completo</option>
                        </select>
                    </div>
                    <div class="mt-[20px]">
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            Especialidade:
                        </label>
                        <select
                            v-model="FormData.specialty"
                            class="w-full sm:w-[432px] px-2 py-1 border rounded-2xl">
                            <option value="Oftalmologia">Oftalmologia</option>
                            <option value="Clinico Geral">Clinico Geral</option>
                        </select>
                    </div>
                    <div class="mt-[20px]">
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            Documento comprobatórios:
                        </label>
                        <div class="flex flex-col items-start">
                            <label
                                for="file-upload"
                                class="px-4 py-2 text-lg text-black bg-white rounded-full border border-gray-300 cursor-pointer sm:rounded-lg hover:bg-gray-100">
                                Anexar
                            </label>
                            <input
                                @change="onFileChange"
                                type="file"
                                id="file-upload"
                                class="hidden" />
                            <span v-if="FormData.fileName" class="text-gray-700">
                                {{ FormData.fileName }}
                            </span>
                        </div>
                    </div>
                    <div class="mt-[20px]">
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            CRM:
                        </label>
                        <input
                            v-model="FormData.crm"
                            type="text"
                            class="px-2 py-1 w-full rounded-2xl border"
                            placeholder="999.999.999-99" />
                        <div v-if="formErrors.crm" class="mt-1 text-sm text-red-500">
                            {{ formErrors.crm }}
                        </div>
                    </div>
                    <div>
                        <label
                            class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
                            Senha:
                        </label>
                        <input
                            v-model="FormData.password"
                            type="password"
                            class="px-2 py-1 w-full rounded-2xl border"
                            placeholder="Digite a senha" />
                        <div v-if="formErrors.password" class="mt-1 text-sm text-red-500">
                            {{ formErrors.password }}
                        </div>
                    </div>
                    <button
                        class="mt-[40px] bg-[#00428F] text-white w-[104px] h-[42px] rounded-lg btn"
                        @click="submitForm">
                        Cadastrar
                    </button>
                    <dialog id=" my_modal_4" class="modal" ref="modal" @click.self="closeModal">
                        <div class="modal-box w-[310px] sm:w-[750px] max-w-5xl">
                            <div>
                                <h1
                                    class="font-montserrat text-[1.375rem] font-semibold text-center">
                                    Médico cadastrado com sucesso!
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

                                <h2
                                    class="mt-[40px] mb-4 text-xl font-montserrat text-black font-bold">
                                    Dados Profissionais:
                                </h2>

                                <div class="flex flex-col">
                                    <label
                                        class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
                                        Formação:
                                    </label>
                                    <p>
                                        {{ FormData.degree }}
                                    </p>
                                </div>
                                <div class="flex flex-col">
                                    <label
                                        class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
                                        Especialidade:
                                    </label>
                                    <p>
                                        {{ FormData.specialty }}
                                    </p>
                                </div>
                                <div class="flex flex-col">
                                    <label
                                        class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
                                        Documentos comprobatórios:
                                    </label>

                                    <p
                                        class="border rounded-3xl p-4 w-[160px]"
                                        :style="{ borderColor: '#010424', color: '#010424' }">
                                        {{
                                            FormData.uploadedFile?.name ||
                                            'Nenhum arquivo carregado'
                                        }}
                                    </p>
                                </div>

                                <div class="flex flex-col">
                                    <label
                                        class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
                                        CRM:
                                    </label>
                                    <p>
                                        {{ FormData.crm }}
                                    </p>
                                </div>
                            </ModalCadastro>
                            <div class="flex flex-col justify-between modal-action">
                                <div class="flex w-full pl-[50px] justify-center sm:justify-start">
                                    <form method="dialog">
                                        <!-- if there is a button, it will close the modal -->
                                        <button
                                            @click="closeModal"
                                            class="bg-[#00428F] text-white w-[104px] h-[42px] rounded-lg mt-auto">
                                            Fechar
                                        </button>
                                    </form>
                                    <form method="dialog" class="modal-backdrop">
                                        <button>Fechar</button>
                                    </form>
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
    shifts: '',
    plantoes: '',
    degree: 'Graduação Completa',
    specialty: 'Oftalmologia',
    uploadedFile: null as File | null,
    fileName: '',
    crm: '',
    password: ''
})

//Constante para manipular modal e poder fechar ao clicar fora do modal
const modal = ref<HTMLDialogElement | null>(null)

//função para fechar ao clicar fora
const closeModal = () => {
    modal.value?.close()
}

// adiciona refs para controle de validação
const formErrors = ref<Record<string, string>>({})

const validateForm = () => {
    formErrors.value = {}

    // validação de campos obrigatórios
    if (!FormData.fullName) {
        formErrors.value.fullName = 'nome completo é obrigatório'
    }
    if (!FormData.email) {
        formErrors.value.email = 'email é obrigatório'
    }
    if (!FormData.cpf) {
        formErrors.value.cpf = 'cpf é obrigatório'
    }
    if (!FormData.crm) {
        formErrors.value.crm = 'crm é obrigatório'
    }
    if (!FormData.password) {
        formErrors.value.password = 'senha é obrigatória'
    }

    // retorna true se não houver erros
    return Object.keys(formErrors.value).length === 0
}

const submitForm = async () => {
    try {
        // valida o formulário antes de enviar
        if (!validateForm()) {
            toast.error('por favor, preencha todos os campos obrigatórios')
            return
        }

        // prepara os dados para envio
        const doctorData = {
            first_name: FormData.fullName.split(' ')[0],
            last_name: FormData.fullName.split(' ').slice(1).join(' '),
            email: FormData.email,
            cpf: FormData.cpf,
            date_birth: FormData.dateOfBirth,
            gender: FormData.gener,
            formacao: FormData.degree,
            crm: FormData.crm,
            roles: [
                {
                    name: 'DOCTOR'
                }
            ],
            address: {
                country: FormData.country,
                state: FormData.state,
                city: FormData.city,
                neighborhood: FormData.neighborhood,
                street: FormData.street,
                number: FormData.number,
                zip_code: FormData.zipCode
            },
            //attach_document: FormData.uploadedFile,
            password: FormData.password
        }

        let response = await userStore.createDoctor(doctorData)
        console.log(response)
        toast.success('médico cadastrado com sucesso!')
        modal.value?.showModal()
    } catch (error) {
        if (userStore.validationErrors) {
            // exibe erros específicos do backend
            Object.entries(userStore.validationErrors).forEach(([field, errors]) => {
                formErrors.value[field] = errors[0]
            })
            toast.error('verifique os campos com erro')
        } else {
            toast.error('erro ao cadastrar médico')
        }
        console.error(error)
    }
}

const onFileChange = async (event: Event) => {
    const input = event.target as HTMLInputElement
    if (input.files && input.files.length > 0) {
        const file = input.files[0]
        FormData.fileName = file.name

        const reader = new FileReader()
        reader.readAsDataURL(file)

        reader.onload = () => {
            const base64String = reader.result as string
            FormData.uploadedFile = base64String.split(',')[1] || base64String
        }

        reader.onerror = (error) => {
            console.error('Error converting file to base64:', error)
            toast.error('Erro ao processar o arquivo')
        }
    }
}
</script>

<style scoped>
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
