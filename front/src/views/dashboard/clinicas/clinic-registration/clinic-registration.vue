<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Card, CardContent } from '@/components/ui/card'
import { PersonalData, AddressData } from '@/components/commons'
</script>

<template>
    <LayoutDashboard>
        <div class="max-w-3xl mx-auto my-10">
            <div class="mb-8">
                <h1 class="text-3xl font-bold">Cadastrar Clínica</h1>
                <p class="text-sm text-gray-500">
                    Preencha as informações abaixo para poder cadastrar uma nova clínica
                </p>
            </div>

            <form class="max-w-3xl mx-auto my-10">
                <Card>
                    <CardContent class="p-6 space-y-6">
                        <PersonalData :isFieldDirty="isFieldDirty" />
                        <AddressData :isFieldDirty="isFieldDirty" />
                    </CardContent>
                </Card>
            </form>
        </div>
    </LayoutDashboard>
</template>
