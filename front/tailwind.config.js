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
	],

	theme: {
		extend: {
			colors: {
				primary: '#00428F',
				lightGreen: '#BBFAE4',
				lightBlue: '#DEECFA'
			},
			fontFamily:{
				montserrat:['Montserrat', 'sans-serif'],
				openSans:['Open sans'],
				roboto:['Roboto', 'sans-serif']
			}
		},
	},


	plugins: [daisyui],
	daisyui: {
		themes: ["light"],
	},
}
