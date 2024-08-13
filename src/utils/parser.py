import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', type=str, default='book')
    parser.add_argument('--data_dir', type=str, default='..\\data\\')
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--seed', type=int, default=2023)
    parser.add_argument('--inverse_r', type=int, default=1)
    
    parser.add_argument('--n_epochs', type=int, default=1000)
    parser.add_argument('--batch_size', type=int, default=2048)
    parser.add_argument('--test_batch_size', type=int, default=8192)
    
    parser.add_argument('--emb_size', type=int, default=128)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--l2_decay', type=float, default=1e-5)
    parser.add_argument('--tau', type=float, default=1)
    parser.add_argument('--cl_decay', type=float, default=1e-6)
    parser.add_argument('--cg_decay', type=float, default=0.0001)

    parser.add_argument('--w_cg', type=float, default=0.001)
    parser.add_argument('--w_kg', type=float, default=0.1)
    parser.add_argument('--cor_user_cg', type=float, default=0.0001)
    parser.add_argument('--cor_item_cg', type=float, default=0.005)
    parser.add_argument('--cor_user_kg', type=float, default=0.0005)
    parser.add_argument('--cor_item_kg', type=float, default=0.0005)

    parser.add_argument('--mess_dropout', type=int, default=1)
    parser.add_argument('--mess_dropout_rate', type=float, default=0.1)
    
    parser.add_argument('--n_hops_cg', type=int, default=3)
    parser.add_argument('--n_hops_kg', type=int, default=3)
    
    parser.add_argument('--n_heads', type=int, default=2)

    parser.add_argument('--node_dropout', type=int, default=1)
    parser.add_argument('--node_dr_kg', type=float, default=0.5)
    parser.add_argument('--kg_agg_type', type=str, default='neigh')

    parser.add_argument('--node_dr_cg', type=float, default=0.5)
    parser.add_argument('--cg_agg_type', type=str, default='neigh')

    parser.add_argument('--node_dr_pf', type=float, default=0.5)

    parser.add_argument('--attn_dr', type=float, default=0.5)

    parser.add_argument('--rep_type', type=str, default='sumup')

    parser.add_argument('--show_steps', type=int, default=10)
    parser.add_argument('--k_list', type=str, default='[5,10,20,50,100]')

    args = parser.parse_args()

    return args
    
