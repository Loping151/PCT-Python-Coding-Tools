# PCT-Python-Coding-Tools

<details>
<summary>cuda_free</summary>

wrapper `cuda_free_always`

usage: `cuda_free_always(your_train_func)(your train args)`

Sometimes people prefer to stop training or other running code with Ctrl-Z instead of Ctrl-C because it responds faster and always works. However, since Ctrl-Z allows you to resume a process with bg, the resources (such as CUDA memory) are not released. We'll have to kill the process or the bash. This wrapper helps ensure memory release after Ctrl-Z and Ctrl-C, but please note that resuming is no longer supported.

</details>
