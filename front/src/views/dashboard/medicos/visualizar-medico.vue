<script setup lang="ts">
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
</script>

<template>
    <LayoutDashboard>
        <form class="max-w-3xl mx-auto my-10">
            <div class="flex items-center justify-between mb-4">
                <div class="flex gap-4 items-center">
                    <Avatar size="base" class="bg-primary text-white">
                        <AvatarImage src="https://github.com/josmartrigueiro.pnag" alt="@unovue" />
                        <AvatarFallback>JS</AvatarFallback>
                    </Avatar>
                    <div>
                        <h2 class="text-3xl font-bold">Dr. João Ribeiro</h2>
                        <div class="text-sm text-gray-500">Recepcionista</div>
                    </div>
                </div>
            </div>

            <Tabs default-value="personal">
                <TabsList
                    className="grid grid-cols-2 mb-4 border rounded-md p-1.5 border-gray-200 bg-white">
                    <TabsTrigger value="personal">Dados Pessoais</TabsTrigger>
                    <TabsTrigger value="work">Expediente</TabsTrigger>
                </TabsList>

                <TabsContent value="personal">adsf</TabsContent>
                <TabsContent value="work">asdf</TabsContent>
            </Tabs>
        </form>
    </LayoutDashboard>
</template>
