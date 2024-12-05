<template>
    
    <LayoutDashboard>
        <div class="ml-[37px] mt-[54px]">
            <div class="flex gap-3">
                <router-link to="/dashboard/suporte/escolher-perfil">
                    <h2 class="text-xl font-light text-[#00428F] hover:text-gray-800 transition duration-300 ease-in-out font-montserrat">
                        < Suporte ao usuário</h2>
                </router-link>
                <router-link to="/dashboard/suporte/faq">
                    <h2 class="text-xl font-light text-[#00428F] hover:text-gray-800 transition duration-300 ease-in-out font-montserrat">
                        < FAQ</h2>
                </router-link>
            </div>
            <div class="ml-[112px] mt-[27px]">
                <h1 class="font-montserrat text-[#00428F] font-bold text-[2.5rem]">Editar Perguntas</h1>

                <div class="bg-white w-[669px] h-[747px] flex justify-center">
                    <form class="w-[573px] space-y-[20px] mt-[51.5px]">
                        <div class="flex flex-col space-y-[16px]">
                            <label for="titulo" class="font-montserrat text-2xl font-light text-black">Titulo:</label>
                            <input type="text" id="titulo" name="titulo" 
                            class="font-montaserrat text-xl  border-2 border-black rounded-xl h-[35px] pl-[26px] placeholder-shown:font-montaserrat placeholder-shown:text-xl	"
                            value="What is Loren ipsum" >
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="pergunta" class="font-montserrat text-2xl font-light text-black">Perguntas: </label>
                            <input type="text" id="pergunta" name="pergunta" value="What is Loren ipsum?" class="border-2 border-black rounded-xl h-[35px] pl-[26px] font-montaserrat text-xl placeholder-shown:font-montaserrat placeholder-shown:text-xl">
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="conteudo" class="font-montserrat text-2xl font-light text-black">Conteudo:</label>
                            <textarea name="conteudo" id="conteudo"  class=" font-montaserrat text-xl  border-2 border-black rounded-xl h-[150px] resize-none pl-[26px] pt-[21px] placeholder-shown:font-montaserrat placeholder-shown:text-xl	"
                            value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut"></textarea>
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="perfil" class="font-montserrat text-2xl font-light text-black">Pefil:</label>
                            <select id="perfil" name="perfil" class="border-2 border-black rounded-xl h-[35px] pl-[26px] font-montserrat text-2xl font-light">
                                <option value="Nenhum" selected class="font-montserrat text-2xl font-light">Nenhum</option>
                                <option value="administrador" class="font-montserrat text-2xl font-light">Administrador</option>
                                <option value="clinica" class="font-montserrat text-2xl font-light">Clinica</option>
                                <option value="paciente" class="font-montserrat text-2xl font-light">Paciente</option>
                            </select>
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="tags" class="font-montserrat text-2xl font-light text-black">Tags:</label>
                            <input type="text" id="tags" name="tags" placeholder="Digite as #tags" class="border-2 border-black rounded-xl h-[35px] pl-[26px] placeholder-shown:font-montaserrat placeholder-shown:text-xl	font-montaserrat text-xl "
                            value="#tag1">
                        </div>
                        <div class="flex justify-between mt-[23px]">
                            <button class="w-[130px] h-[33px] rounded-m bg-[#26438B] text-white rounded-xl font-montserrat text-lg font-medium">Cadastrar</button>
                            <button class="w-[203px] h-[33px] rounded-m bg-[#26438B] text-white rounded-xl font-montserrat text-lg font-medium">Salvar e cadastrar</button>
                        </div>
                    </form>
                </div>
            </div>
            
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue';


</script>