import daisyui from "daisyui"

/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: ["class"],
	safelist: ["dark"],
	prefix: "",

	content: [
		'./pages/**/*.{ts,tsx,vue}',
		'./components/**/*.{ts,tsx,vue}',
		'./app/**/*.{ts,tsx,vue}',
		'./src/**/*.{ts,tsx,vue}',
		'.index.html',
		'./.src/**/*.{vue,js,ts,jsx,tsx}',
	],

	theme: {
		extend: {
			colors: {
				primary: '#00428F',
				lightGreen: '#BBFAE4',
				lightBlue: '#DEECFA',
				DeepBlue: '#26438B',
			},
			fontFamily:{
				montserrat:['Montserrat', 'sans-serif'],
				openSans:['Open sans'],
				roboto:['Roboto', 'sans-serif'],
				raleway:['Raleway', 'sans-serif']
			}
		},
	},


	plugins: [daisyui],
	daisyui: {
		themes: ["light"],
	},
}
