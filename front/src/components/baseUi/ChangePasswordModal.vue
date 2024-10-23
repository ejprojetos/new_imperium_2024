<template>
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
        <div class="p-6 bg-white rounded-lg shadow-lg w-96">
            <h2 class="mb-4 text-xl font-semibold">Alterar Senha</h2>
            <form @submit.prevent="changePassword">
                <div class="mb-4">
                    <label for="currentPassword" class="block mb-1 font-semibold">
                        Senha Atual:
                    </label>
                    <input
                        v-model="currentPassword"
                        type="password"
                        id="currentPassword"
                        required
                        class="w-full px-2 py-1 border rounded" />
                </div>
                <div class="mb-4">
                    <label for="newPassword" class="block mb-1 font-semibold">Nova Senha:</label>
                    <input
                        v-model="newPassword"
                        type="password"
                        id="newPassword"
                        required
                        class="w-full px-2 py-1 border rounded" />
                </div>
                <div class="mb-4">
                    <label for="confirmPassword" class="block mb-1 font-semibold">
                        Confirmar Nova Senha:
                    </label>
                    <input
                        v-model="confirmPassword"
                        type="password"
                        id="confirmPassword"
                        required
                        class="w-full px-2 py-1 border rounded" />
                </div>
                <div class="flex justify-end">
                    <button
                        type="button"
                        @click="$emit('close')"
                        class="px-4 py-2 mr-2 text-gray-700 bg-gray-200 rounded">
                        Cancelar
                    </button>
                    <button type="submit" class="px-4 py-2 text-white bg-blue-600 rounded">
                        Salvar
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const currentPassword = ref('')
const newPassword = ref('')
const confirmPassword = ref('')

const emit = defineEmits(['close', 'password-changed'])

function changePassword() {
    if (newPassword.value !== confirmPassword.value) {
        alert('As senhas não coincidem. Por favor, tente novamente.')
        return
    }

    console.log('Changing password:', {
        currentPassword: currentPassword.value,
        newPassword: newPassword.value
    })

    emit('password-changed') // leva para o componente pai
}
</script>
