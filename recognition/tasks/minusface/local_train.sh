export CUDA_VISIBLE_DEVICES=''
python3 -u -m torch.distributed.launch --nproc_per_node=1 --nnodes=1 --use_env train.py