import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import stylistic from '@stylistic/eslint-plugin'
import tseslint from 'typescript-eslint'

export default tseslint.config(
  { ignores: ['dist'] },
  {
    extends: [
      js.configs.recommended,
      ...tseslint.configs.strict,
      ...tseslint.configs.stylistic,
    ],
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      '@stylistic': stylistic,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
      // Stylistic rules
      "@stylistic/array-bracket-newline": ["error", "consistent"],
      "@stylistic/array-bracket-spacing": ["error", "never"],
      "@stylistic/array-element-newline": ["error", "consistent"],
      "@stylistic/brace-style": ["error", "1tbs", { allowSingleLine: true }],
      "@stylistic/comma-dangle": ["error", "always-multiline"],
      "@stylistic/eol-last": ["error", "always"],
      "@stylistic/indent": ["error", 2],
      "@stylistic/jsx-quotes": ["error", "prefer-double"],
      "@stylistic/no-multi-spaces": ["error"],
      "@stylistic/no-multiple-empty-lines": ["error", { max: 1 }],
      "@stylistic/no-trailing-spaces": ["error"],
      "@stylistic/object-curly-newline": ["error", { "consistent": true }],
      "@stylistic/object-property-newline": ["error", { allowAllPropertiesOnSameLine: true }],
      "@stylistic/object-curly-spacing": ["error", "always"],
      "@stylistic/quotes": ["error", "double"],
      "@stylistic/semi": ["error", "never"],
    },
  },
)
