module.exports = {
  extends: ['plugin:@typescript-eslint/recommended'],
  parserOptions: {
    ecmaVersion: 11,
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint'],
  rules: {
    '@typescript-eslint/no-empty-function': ['error', { allow: ['methods', 'arrowFunctions'] }],
    '@typescript-eslint/no-unused-vars': ['error'],
    '@typescript-eslint/no-explicit-any': ['error'],
    'no-console': ['error'],
    'no-debugger': ['error'],
    '@typescript-eslint/explicit-module-boundary-types': 'off',
  },
};