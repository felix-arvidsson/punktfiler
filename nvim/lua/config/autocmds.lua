-- Autocmds are automatically loaded on the VeryLazy event
-- Default autocmds that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/autocmds.lua
-- Add any additional autocmds here

-- Set indentation settings for .gd files
vim.cmd([[
  autocmd FileType gd setlocal tabstop=4 softtabstop=4 shiftwidth=4 expandtab=false
]])

