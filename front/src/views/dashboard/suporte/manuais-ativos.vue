<template>
    <LayoutDashboard>
        <div class="flex items-center mb-6 w-full max-w-[1000px] m-6">
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

        <!-- AQUI COMEÇA A PÁGINA -->
        <div
            class="bg-[#E2EAF6] w-[70%] h-[39px] flex gap-5 items-center rounded-full pl-[17px] pr-[5px] ml-[85px]">
            <input
                type="text"
                name="busca-manual"
                id="busca-manual"
                class="bg-[transparent] w-[100%] h-[23px] border-[#26438B]"
                placeholder="Buscar manual" />
            <font-awesome-icon :icon="['fas', 'magnifying-glass']" />
            <Search class="w-22" />
            <button class="bg-[#00428F] text-white w-[121px] rounded-xl">Pesuisar</button>
        </div>

        <div class="ml-[112px] mt-[27px]">
            <!-- MANUAIS ATIVOS -->
            <h1 class="font-montserrat text-[#00428F] font-bold text-[2rem]">Manuais ativos</h1>

            <div class="bg-white w-[70%] h-[138px] flex items-center justify-center">
                <div class="cards-ativos h-[66px] flex w-[90%] items-center">
                    <div class="w-[3px] bg-[#71C285] h-[90%]"></div>
                    <span class="font-montserrat text-[10px] text-[#CCCCCC]">10/10/2024</span>
                    <div class="w-[1px] h-[90%] bg-[#CCCCCC]"></div>
                    <div class="w-[70%]">
                        <h3 class="font-montserrat text-3xl font-medium">MANUAL DO MÉDICO</h3>
                    </div>
                    <button class="w-[79px] bg-[#6CA6D0] text-white rounded-full">Editar</button>
                    <button>
                        <Trash2 class="w-[20px] h-[20px] text-red-500" />
                    </button>
                </div>
            </div>

            <!-- MANUAIS INATIVOS -->
            <h1 class="font-montserrat text-[#00428F] font-bold text-[2rem] mt-[139px]">Manuais inativos</h1>

            <div class="bg-white w-[70%] h-[138px] flex items-center justify-center">
                <div class="cards-ativos h-[66px] flex w-[90%] items-center">
                    <div class="w-[3px] bg-[#FA4954] h-[90%]"></div>
                    <span class="font-montserrat text-[10px] text-[#CCCCCC]">10/10/2024</span>
                    <div class="w-[1px] h-[90%] bg-[#CCCCCC]"></div>
                    <div class="w-[70%]">
                        <h3 class="font-montserrat text-3xl font-medium">MANUAL DO MÉDICO</h3>
                    </div>
                    <button class="w-[79px] bg-[#6CA6D0] text-white rounded-full">Editar</button>
                    <button>
                        <Trash2 class="w-[20px] h-[20px] text-red-500" />
                    </button>
                </div>
            </div>

            <div class="bg-white w-[70%] h-[138px] flex items-center justify-center">
                <div class="cards-ativos h-[66px] flex w-[90%] items-center">
                    <div class="w-[3px] bg-[#FA4954] h-[90%]"></div>
                    <span class="font-montserrat text-[10px] text-[#CCCCCC]">10/10/2024</span>
                    <div class="w-[1px] h-[90%] bg-[#CCCCCC]"></div>
                    <div class="w-[70%]">
                        <h3 class="font-montserrat text-3xl font-medium">MANUAL DO MÉDICO</h3>
                    </div>
                    <button class="w-[79px] bg-[#6CA6D0] text-white rounded-full">Editar</button>
                    <button>
                        <Trash2 class="w-[20px] h-[20px] text-red-500" />
                    </button>
                </div>
            </div>

            <div class="bg-white w-[70%] h-[138px] flex items-center justify-center">
                <div class="cards-ativos h-[66px] flex w-[90%] items-center">
                    <div class="w-[3px] bg-[#FA4954] h-[90%]"></div>
                    <span class="font-montserrat text-[10px] text-[#CCCCCC]">10/10/2024</span>
                    <div class="w-[1px] h-[90%] bg-[#CCCCCC]"></div>
                    <div class="w-[70%]">
                        <h3 class="font-montserrat text-3xl font-medium">MANUAL DO MÉDICO</h3>
                    </div>
                    <button class="w-[79px] bg-[#6CA6D0] text-white rounded-full">Editar</button>
                    <button>
                        <Trash2 class="w-[20px] h-[20px] text-red-500" />
                    </button>
                </div>
            </div>

            <div class="bg-white w-[70%] h-[138px] flex items-center justify-center">
                <div
                class="bg-[#E2EAF6] w-[70%] h-[39px] flex gap-5 items-center justify-center rounded-full">
                    <button>1</button>
                    <button>2</button>
                    <button>3</button>
                    <button>4</button>
                    <button>5</button>
            </div>

            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search } from 'lucide-vue-next'
import { Trash2 } from 'lucide-vue-next'
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
