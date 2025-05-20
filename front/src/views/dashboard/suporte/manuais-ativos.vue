<template>
    <LayoutDashboard>
        <div class="flex items-center justify-between mb-6 w-full max-w-[1000px] m-6">
            <div class="flex ">
                <RouterLink
                    to="/dashboard/suporte/administrador"
                    class="flex items-center text-blue-600 hover:text-blue-800 mb-4">
                    <span class="mr-2"></span>
                    <span>< Suporte ao usuário</span>
                </RouterLink>
                <RouterLink
                    to="/dashboard/suporte/manuais"
                    class="flex items-center text-blue-600 hover:text-blue-800 mb-4">
                    <span class="mr-2"></span>
                    <span>< Manuais</span>
                </RouterLink>
            </div>
            <div class="mr-[40px]">
                <RouterLink
                    to="/dashboard/suporte/editar-manuais"
                    class="flex items-center text-blue-600 hover:text-blue-800 mb-4">
                    <button class="h-[40px] w-[200px] bg-[#6CA6D0] text-white rounded-full hover:bg-green-500">Cadastrar Novo Manual</button>
                </RouterLink>
            </div>
        </div>

        <!-- AQUI COMEÇA A PÁGINA -->
        <div 
        v-if="todosManuais.length === 0">
             <h1 class="font-montserrat text-[#00428F] font-bold text-[2rem]">SEM MANUAIS CADASTRADOS</h1>
        </div>
        <div class="ml-[112px] mt-[27px]"
        v-if="todosManuais.length > 0">
            <div v-if="paginaAtual === 1">
                <!-- MANUAIS ATIVOS -->
                <h1 class="font-montserrat text-[#00428F] font-bold text-[2rem]">Manuais ativos</h1>
                <div
                v-for="manual in manuaisAtivos" 
                :key="manual.id" 
                class="bg-white w-[70%] h-[138px] flex items-center justify-center">
                    <div class="cards-ativos h-[66px] flex w-[90%] items-center">
                        <div class="w-[3px] bg-[#71C285] h-[90%]"></div>
                        <span class="font-montserrat text-[10px] text-[#CCCCCC]">10/10/2024</span>
                        <div class="w-[1px] h-[90%] bg-[#CCCCCC]"></div>
                        <div class="w-[70%]">
                            <h3 class="font-montserrat text-3xl font-medium">{{manual.title}}</h3>
                        </div>
                        <RouterLink
                            :to="`/dashboard/suporte/editar-manuais/${manual.id}`"
                            class="flex items-center text-blue-600 hover:text-blue-800">
                            <button class="w-[79px] bg-[#6CA6D0] text-white rounded-full">Editar</button>
                        </RouterLink>
                        <button>
                            <Trash2 class="w-[20px] h-[20px] text-red-500" />
                        </button>
                    </div>
                </div>
            </div>

            <!-- MANUAIS INATIVOS -->
            <h1 class="font-montserrat text-[#00428F] font-bold text-[2rem] mt-[40px]">Manuais inativos</h1>

            <div v-for="manual in manuaisInativos" :key="manual.id"
            class="bg-white w-[70%] h-[138px] flex items-center justify-center">
                <div class="cards-ativos h-[66px] flex w-[90%] items-center">
                    <div class="w-[3px] bg-[#FA4954] h-[90%]"></div>
                    <span class="font-montserrat text-[10px] text-[#CCCCCC]">10/10/2024</span>
                    <div class="w-[1px] h-[90%] bg-[#CCCCCC]"></div>
                    <div class="w-[70%]">
                        <h3 class="font-montserrat text-3xl font-medium">{{ manual.title }}</h3>
                    </div>
                    <RouterLink
                        :to="`/dashboard/suporte/editar-manuais/${manual.id}`"
                        class="flex items-center text-blue-600 hover:text-blue-800">
                        <button class="w-[79px] bg-[#6CA6D0] text-white rounded-full">Editar</button>
                    </RouterLink>
                    <button>
                        <Trash2 class="w-[20px] h-[20px] text-red-500" />
                    </button>
                </div>
            </div>

            <div class="bg-white w-[70%] h-[138px] flex items-center justify-center">
            
            <div class="bg-[#E2EAF6] w-[70%] h-[39px] flex gap-5 items-center justify-center rounded-full">
                <button @click="carregarPagina(paginaAtual - 1)" :disabled="paginaAtual === 1">
                    Anterior
                </button>
                <button v-for="pagina in Math.ceil(todosManuais.length / itensPorPagina)" :key="pagina"
                    @click="carregarPagina(pagina)"
                    :class="{ 'font-bold': pagina === paginaAtual }">
                    {{ pagina }}
                </button>
                <button @click="carregarPagina(paginaAtual + 1)" :disabled="paginaAtual === Math.ceil(todosManuais.length / itensPorPagina)">
                    Próxima
                </button>
            </div>


            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import {  manualService } from '@/services/ajuda.service'
import { useManualStore } from '@/stores/ajuda/manualStore'
import { perfilSelecionado} from '@/stores/ajuda/perfilStore'
import { Trash2 } from 'lucide-vue-next'
import { computed, onMounted, ref } from 'vue'

const manualStore = useManualStore()
const manual = ref<Manual | null>(null)
const manuais = ref<Manual[]>([])
const manuaisAtivos = ref<Manual[]>([])
const manuaisInativos = ref<Manual[]>([])

// Perfil hardcoded
const userProfile = 'ADMIN'

const optionSelected = ref({
    perfil: perfilSelecionado.value
})
console.log('PERFIL SELECIONADO: ',perfilSelecionado.value)


const todosManuais = ref<Manual[]>([]);
const paginaAtual = ref(1);
const itensPorPagina = 5;

const carregarTodosManuais = async () => {
    let pagina = 1;
    let tempManuais: Manual[] = [];
    let temProxima = true;

    while (temProxima) {
        const resposta = await manualService.getAllManuals(pagina);
        tempManuais = tempManuais.concat(resposta.results);

        if (resposta.next) {
            pagina++;
        } else {
            temProxima = false;
        }
    }

    // ✅ Filtra manuais pelo perfil selecionado
    const manuaisFiltrados = tempManuais.filter(manual => manual.profile === optionSelected.value.perfil).sort((a, b) => b.id - a.id);

    todosManuais.value = manuaisFiltrados;

    // Atualiza o que mostrar na página atual
    atualizarManuaisPagina();
};


const manuaisPaginaAtual = computed(() => {
    const start = (paginaAtual.value - 1) * itensPorPagina;
    const end = start + itensPorPagina;
    return todosManuais.value.slice(start, end);
});

const atualizarManuaisPagina = () => {
    const pagina = manuaisPaginaAtual.value;

    if (pagina.length > 0) {
        if(paginaAtual.value === 1){
           manuaisAtivos.value = [pagina[0]];  // o primeiro da página é ativo
        }
        manuaisInativos.value = pagina.slice(1); // resto inativos
    } else {
        manuaisAtivos.value = [];
        manuaisInativos.value = [];
    }
};


const carregarPagina = (pagina: number) => {
    if (pagina < 1 || pagina > Math.ceil(todosManuais.value.length / itensPorPagina)) {
        return;
    }
    paginaAtual.value = pagina;
    atualizarManuaisPagina();
};



onMounted(async () => {
    //carregarPagina(1);
    await carregarTodosManuais();
//   try {
//     await manualStore.fetchManuals(1)
//     // Filtra manuais pelo profile
//     const filteredManuais = manualStore.manuals.filter(manual => manual.profile === userProfile)
    
//     // Ordena manuais por data de cadastro, assumindo que manual tem um campo 'createdAt' tipo Date ou string ISO
//     filteredManuais.sort((a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime())
    
//     // O último manual cadastrado é o primeiro após a ordenação decrescente
//     if (filteredManuais.length > 0) {
//       manuaisAtivos.value = [filteredManuais[0]]
//       manuaisInativos.value = filteredManuais.slice(1)
//     } else {
//       manuaisAtivos.value = []
//       manuaisInativos.value = []
//     }

//     manuais.value = filteredManuais
//     console.log('Manuais ativos:', manuaisAtivos.value)
//     console.log('Manuais inativos:', manuaisInativos.value)
//   } catch (error) {
//     console.error('Erro ao buscar manuais', error)
//   }
})


</script>

<style scoped>
#busca-manual {
    border: solid 1px #26438b;
    border-radius: 50px;
    padding-left: 10px;
}
#busca-manual:hover {
    border: solid 1px #26438b;
}

.cards-ativos {
    padding: 0px;
    gap: 12px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;
}
</style>
