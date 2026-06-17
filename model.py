"""
AlphaZero on Connect-4 from Scratch

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - make_empty_board
import numpy as np

def make_empty_board():
    """Return a 6x7 integer numpy array of zeros representing an empty Connect-4 board."""
    # TODO: create a 6x7 integer array of zeros and return it
    arr=np.zeros((6,7),dtype=int)
    return arr

# Step 2 - column_top_row
def column_top_row(board, column):
    """Return the lowest empty row in `column`, or -1 if the column is full."""
    # TODO: scan the column from the bottom up and return the first empty row index
    for row in range(len(board)-1,-1,-1):
        if board[row][column]==0: 
            return row
    return -1

# Step 3 - drop_piece
import copy

def drop_piece(board, column, player):
    board_copy=copy.deepcopy(board)
    
    for row in range(len(board_copy)-1, -1, -1):
        if board_copy[row][column]==0:
            board_copy[row][column]=player
            break 
    else:
        raise ValueError("")
        
    return board_copy

# Step 4 - column_full
import numpy as np

def column_full(board, column):
    """Return True if `column` has no empty rows left."""
    # TODO: check whether the column can still accept a piece
    return bool(np.all(board[:,column]!=0))

# Step 5 - valid_moves
def valid_moves(board):
    # TODO: return a list of column indices that still have at least one empty row
    return [col for col in range(len(board[0])) if any(board[row][col]==0 for row in range(len(board)))]

# Step 6 - four_in_a_row_horizontal
import numpy as np

def four_in_a_row_horizontal(board):
    # TODO: scan every row for four consecutive matching non-zero pieces horizontally
    if board is None or len(board)==0:
        return None
        
    rows=len(board)
    cols=len(board[0])
    
    for r in range(rows):
        for c in range(cols-3):
            window=board[r][c:c+4]
            first_element=window[0]
            if first_element!=0 and np.all(window==first_element):
                return int(first_element) 
                
    return 0

# Step 7 - four_in_a_row_vertical
def four_in_a_row_vertical(board):
    # TODO: scan every column for four consecutive matching non-zero pieces vertically
    if board is None or len(board)==0:
        return None
        
    rows=len(board)
    cols=len(board[0])
    
    for r in range(rows-3):
        for c in range(cols):
            window=board[r:r+4,c]
            first_element=window[0]
            if first_element!=0 and np.all(window==first_element):
                return int(first_element) 
                
    return 0

# Step 8 - four_in_a_row_diagonal_down_right
import numpy as np

def four_in_a_row_diagonal_down_right(board):
    # TODO: scan every down-right diagonal of the 6x7 board for four matching non-zero pieces
    if board is None or len(board)==0:
        return None
        
    rows=len(board)
    cols=len(board[0])

    for r in range(rows-3):
        for c in range(cols-3):
            sub_grid=board[r:r+4,c:c+4]
            
            window=np.diag(sub_grid)
            first_element=window[0]
            
            if first_element!=0 and np.all(window==first_element):
                return int(first_element)
                
    return 0

# Step 9 - four_in_a_row_diagonal_up_right
import numpy as np

def four_in_a_row_diagonal_up_right(board):
    # TODO: scan every up-right diagonal for four consecutive matching non-zero pieces
    if board is None or len(board)==0:
        return None
        
    rows=len(board)
    cols=len(board[0])

    for r in range(rows-3):
        for c in range(cols-3):
            sub_grid=board[r:r+4,c:c+4]
            
            window=np.diag(np.fliplr(sub_grid))
            first_element=window[0]
            
            if first_element!=0 and np.all(window==first_element):
                return int(first_element)
                
    return 0

# Step 10 - check_winner
import numpy as np

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # Define helper to check 4 consecutive matching non-zero elements
    def check_line(line):
        for i in range(len(line)-3):
            if line[i]!=0 and line[i]==line[i+1]==line[i+2]==line[i+3]:
                return line[i]
        return 0

    H,W=board.shape

    for row in board:
        winner=check_line(row)
        if winner:return winner

    for col in board.T:
        winner=check_line(col)
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(np.fliplr(board), d))
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(board, d))
        if winner:return winner

    return 0

# Step 11 - board_is_full
def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    return 0 not in board[0,:]

# Step 12 - is_terminal
import numpy as np

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # Define helper to check 4 consecutive matching non-zero elements
    def check_line(line):
        for i in range(len(line)-3):
            if line[i]!=0 and line[i]==line[i+1]==line[i+2]==line[i+3]:
                return line[i]
        return 0

    H,W=board.shape

    for row in board:
        winner=check_line(row)
        if winner:return winner

    for col in board.T:
        winner=check_line(col)
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(np.fliplr(board), d))
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(board, d))
        if winner:return winner

    return 0

def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    return 0 not in board[0,:]


def is_terminal(board):
    # TODO: return (done, winner) using check_winner and board_is_full.
    winner=check_winner(board)
    done=winner!=0 or board_is_full(board)
    return (bool(done),int(winner))

# Step 13 - other_player
def other_player(player):
    # TODO: return the opponent's player code (1 <-> 2)
    if(player==1):
        return 2
    else:
        return 1

# Step 14 - step_env
import numpy as np

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # Define helper to check 4 consecutive matching non-zero elements
    def check_line(line):
        for i in range(len(line)-3):
            if line[i]!=0 and line[i]==line[i+1]==line[i+2]==line[i+3]:
                return line[i]
        return 0

    H,W=board.shape

    for row in board:
        winner=check_line(row)
        if winner:return winner

    for col in board.T:
        winner=check_line(col)
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(np.fliplr(board), d))
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(board, d))
        if winner:return winner

    return 0

def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    return 0 not in board[0,:]


def is_terminal(board):
    # TODO: return (done, winner) using check_winner and board_is_full.
    winner=check_winner(board)
    done=winner!=0 or board_is_full(board)
    return (bool(done),int(winner))

def step_env(board, column, player):
    # TODO: drop piece for player, then return (new_board, done, winner, next_player).
    new_board=drop_piece(board,column,player)
    done,winner=is_terminal(new_board)
    next_player=2 if player==1 else 1
    return (new_board, done, winner, next_player)

# Step 15 - encode_board
def encode_board(board, current_player):
    """Encode a 6x7 board as a (2, 6, 7) float32 tensor from current_player's view."""
    # TODO: build two binary planes (current player, opponent) and stack them
    
    opponent=3-current_player
    channel1=(board==current_player).astype(np.float32)
    channel2=(board==opponent).astype(np.float32)

    return np.stack([channel1,channel2],axis=0)

# Step 16 - board_to_torch_tensor
import torch
import numpy as np
def board_to_torch_tensor(board, current_player):
    # TODO: encode the board and return it as a float32 torch tensor of shape (1, 2, 6, 7).
    opponent=3-current_player
    channel1=(board==current_player).astype(np.float32)
    channel2=(board==opponent).astype(np.float32)

    yo=np.stack([channel1,channel2],axis=0)
    return torch.from_numpy(yo).unsqueeze(0)

# Step 17 - init_conv_backbone
def init_conv_backbone(in_channels=2, hidden_channels=16):
    # Build a small convolutional backbone preserving the 6x7 spatial shape.
    return nn.Sequential(
        nn.Conv2d(in_channels,hidden_channels,kernel_size=3,stride=1,padding=1),
        nn.BatchNorm2d(hidden_channels),
        nn.ReLU(),
        nn.Conv2d(hidden_channels,hidden_channels,kernel_size=3,stride=1,padding=1),
        nn.BatchNorm2d(hidden_channels),
        nn.ReLU()
    )

# Step 18 - init_policy_head
import torch
import torch.nn as nn

def init_policy_head(hidden_channels=16, num_columns=7):
    """Return an nn.Module mapping (B, hidden_channels, 6, 7) -> (B, num_columns) logits."""
    # TODO: build a small policy head that projects backbone features to column logits
    return nn.Sequential(
        nn.Conv2d(hidden_channels,2,kernel_size=1),
        nn.BatchNorm2d(2),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(2*6*7,num_columns)
    )

# Step 19 - init_value_head
import torch
import torch.nn as nn

def init_value_head(hidden_channels=16):
    """Return an nn.Module mapping (B, hidden_channels, 6, 7) -> (B, 1) in (-1, 1)."""
    # TODO: build a value head that collapses backbone features to a single bounded scalar per board.
    return nn.Sequential(
        nn.Conv2d(hidden_channels,2,kernel_size=1),
        nn.BatchNorm2d(2),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(2*6*7,1)
    )

# Step 20 - build_policy_value_net
import torch
import torch.nn as nn

class PolicyValueNet(nn.Module):
    def __init__(self, backbone, policy_head, value_head):
        super().__init__()
        self.backbone=backbone
        self.policy_head=policy_head
        self.value_head=value_head

    def forward(self, x):
        features=self.backbone(x)
        policy=self.policy_head(features)
        value=self.value_head(features)
        return policy,value

def build_policy_value_net(in_channels=2, hidden_channels=16, num_columns=7):
    """Compose backbone + policy head + value head into one nn.Module."""
    backbone=nn.Sequential(
        nn.Conv2d(in_channels,hidden_channels,kernel_size=3,stride=1,padding=1),
        nn.BatchNorm2d(hidden_channels),
        nn.ReLU(),
        nn.Conv2d(hidden_channels,hidden_channels,kernel_size=3,stride=1,padding=1),
        nn.BatchNorm2d(hidden_channels),
        nn.ReLU()
    )
    
    policy_head=nn.Sequential(
        nn.Conv2d(hidden_channels,2,kernel_size=1),
        nn.BatchNorm2d(2),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(2*6*7,num_columns)
    )

    value_head = nn.Sequential(
        nn.Conv2d(hidden_channels,2,kernel_size=1),
        nn.BatchNorm2d(2),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(2*6*7,1)
    )
    
    return PolicyValueNet(backbone,policy_head,value_head)

# Step 21 - policy_value_forward
import torch
import torch.nn as nn

def policy_value_forward(net, encoded_board):
    """Run encoded_board (B,2,6,7) through net and return (logits, value)."""
    # TODO: call the network on the encoded board and return its two outputs
    logits,value=net(encoded_board)
    return logits,value

# Step 22 - action_mask
import numpy as np

def action_mask(board):
    ans=np.array([], dtype=bool)
    
    for col in range(7):
        if board[0, col]==0:
            ans=np.append(ans,True)
        else:
            ans=np.append(ans,False)
                
    return ans

# Step 23 - masked_policy_logits
import torch

def masked_policy_logits(logits, mask):
    """Set logits at illegal columns to -inf.

    logits: torch.Tensor of shape (..., 7)
    mask:   bool array/tensor of shape (7,), True = legal
    returns: torch.Tensor of same shape as logits
    """
    # TODO: replace logits at illegal columns with negative infinity
    if not isinstance(mask,torch.Tensor):
        mask=torch.tensor(mask,dtype=torch.bool,device=logits.device)
    else:
        mask=mask.to(logits.device,dtype=torch.bool)
    return logits.masked_fill(~mask,float('-inf'))

# Step 24 - masked_log_softmax
import torch
import torch.nn.functional as F 

def newlogit(logits,mask):
    if not isinstance(mask,torch.Tensor):
        mask=torch.tensor(mask,dtype=torch.bool,device=logits.device)
    else:
        mask=mask.to(logits.device,dtype=torch.bool)
    return logits.masked_fill(~mask,float('-inf')) 

def masked_log_softmax(logits, mask):
    """Log-softmax of logits with illegal columns (mask=False) forced to -inf."""
    # TODO: mask out illegal columns, then apply log-softmax over the last dim.
    yologit=newlogit(logits,mask)
    lp=F.log_softmax(yologit,dim=-1) 
    return lp

# Step 25 - sample_action_from_policy
import torch

def sample_action_from_policy(logits, mask, temperature=1.0):
    """Sample a legal column from a tempered masked categorical policy."""
    # TODO: scale logits by temperature, mask illegal columns, sample one index
    scaled_logits=logits/max(temperature, 1e-8)
    masked_logits=scaled_logits.masked_fill(~mask,float('-inf'))

    policy_dist=torch.distributions.Categorical(logits=masked_logits)
    sampled_action=policy_dist.sample()
    
    return int(sampled_action.item())

# Step 26 - greedy_action_from_policy
import torch

def greedy_action_from_policy(logits, mask):
    """Return the argmax legal column index from masked policy logits."""
    # TODO: mask out illegal columns then return the argmax as a python int
    masked_logits=logits.masked_fill(~mask,float('-inf')) 
    return int(torch.argmax(masked_logits).item())

# Step 27 - make_mcts_node
def make_mcts_node(prior=0.0, parent=None):
    # TODO: build a dict with prior, visit_count, value_sum, children, and parent fields.
    return dict(prior=prior,visit_count=0,value_sum=0.0,children={},parent=parent)

# Step 28 - node_q_value
def node_q_value(node):
    # TODO: return the mean value Q = value_sum / visit_count, or 0.0 if visit_count == 0
    if(node['visit_count']==0):
        return 0.0
    else:
        return node['value_sum']/node['visit_count']

# Step 29 - ucb_score
import math

def node_q_value(node):
    # TODO: return the mean value Q = value_sum / visit_count, or 0.0 if visit_count == 0
    if(node['visit_count']==0):
        return 0.0
    else:
        return node['value_sum']/node['visit_count']

def ucb_score(parent, child, c_puct=1.5):
    # TODO: return Q(child) + c_puct * prior * sqrt(N_parent) / (1 + N_child)
    return node_q_value(child)+c_puct*child['prior']*math.sqrt(parent['visit_count'])/(1+child['visit_count'])

# Step 30 - select_best_child
import math

def node_q_value(node):
    # TODO: return the mean value Q = value_sum / visit_count, or 0.0 if visit_count == 0
    if(node['visit_count']==0):
        return 0.0
    else:
        return node['value_sum']/node['visit_count']

def ucb_score(parent,child,c_puct=1.5):
    # TODO: return Q(child) + c_puct * prior * sqrt(N_parent) / (1 + N_child)
    return node_q_value(child)+c_puct*child['prior']*math.sqrt(parent['visit_count'])/(1+child['visit_count'])

def select_best_child(node, legal_actions, c_puct=1.5):
    # TODO: return (action, child) maximizing PUCT among legal children of node.
    best_score=-float('inf')
    best_action=None
    best_child=None
    
    for action in legal_actions:
        child=node['children'][action]
        score=ucb_score(node,child,c_puct)
        
        if(score>best_score):
            best_score=score
            best_action=action
            best_child=child
            
    return best_action,best_child

# Step 31 - select_leaf
import math

def node_q_value(node):
    # TODO: return the mean value Q = value_sum / visit_count, or 0.0 if visit_count == 0
    if(node['visit_count']==0):
        return 0.0
    else:
        return node['value_sum']/node['visit_count']

def ucb_score(parent,child,c_puct=1.5):
    # TODO: return Q(child) + c_puct * prior * sqrt(N_parent) / (1 + N_child)
    return node_q_value(child)+c_puct*child['prior']*math.sqrt(parent['visit_count'])/(1+child['visit_count'])

def select_best_child(node, legal_actions, c_puct=1.5):
    # TODO: return (action, child) maximizing PUCT among legal children of node.
    best_score=-float('inf')
    best_action=None
    best_child=None
    
    for action in legal_actions:
        child=node['children'][action]
        score=ucb_score(node,child,c_puct)
        
        if(score>best_score):
            best_score=score
            best_action=action
            best_child=child
            
    return best_action,best_child

def select_leaf(root, c_puct=1.5):
    # TODO: walk down the MCTS tree picking the best PUCT child until a non-expanded node is reached
    current_node=root
    
    while(current_node['children'] is not None and len(current_node['children'])>0):
        legal_actions=list(current_node['children'].keys())
        best_action,best_child=select_best_child(current_node,legal_actions,c_puct)
        current_node=best_child
        
    return current_node

# Step 32 - evaluate_with_network
def evaluate_with_network(net, state, to_play):
    # TODO: run net on encoded state and return (masked priors np.ndarray (7,), value float)
    encoded=encode_board(state, to_play)  
    state_tensor=torch.FloatTensor(encoded).unsqueeze(0) 
    
    with torch.no_grad():
        policy_logits,value_tensor=net(state_tensor)
        
        probs=torch.softmax(policy_logits,dim=1).squeeze(0).numpy()
        value=torch.tanh(value_tensor).item()  
    
    legal_moves=valid_moves(state) 
    mask=np.zeros(7,dtype=np.float32)
    mask[legal_moves]=1.0
    
    masked_priors=probs*mask
    
    sum_priors=np.sum(masked_priors)
    if sum_priors>0:
        masked_priors/=sum_priors
    else:
        masked_priors=mask/np.sum(mask)

    return masked_priors,float(value)

# Step 33 - expand_node
def expand_node(node, priors):
    # TODO: attach a child node for every legal move with the corresponding network prior
    board=node['board']
    player=node['to_play']
    
    for move in valid_moves(board):
        prior=priors[move]
        child=make_mcts_node(prior=float(prior),parent=node)
        
        child['board']=drop_piece(board, move, player)
        child['to_play']=other_player(player)
        
        node['children'][move]=child
        
    node['is_expanded']=True

# Step 34 - backup_value
def make_mcts_node(prior=0.0, parent=None):
    #using visits in make node
    return {
        'prior':prior,
        'visits':0,        
        'value_sum':0.0,
        'children':{},
        'parent':parent
    }

def backup_value(leaf,value):
    current=leaf
    while current is not None:
        current['visits']+=1
        current['value_sum']+=value
        value=-value
        current=current['parent']

# Step 35 - run_one_simulation
import math
import numpy as np
import torch

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # Define helper to check 4 consecutive matching non-zero elements
    def check_line(line):
        for i in range(len(line)-3):
            if line[i]!=0 and line[i]==line[i+1]==line[i+2]==line[i+3]:
                return line[i]
        return 0

    H,W=board.shape

    for row in board:
        winner=check_line(row)
        if winner:return winner

    for col in board.T:
        winner=check_line(col)
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(np.fliplr(board), d))
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(board, d))
        if winner:return winner

    return 0

def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    return 0 not in board[0,:]

def is_terminal(board):
    # TODO: return (done, winner) using check_winner and board_is_full.
    winner=check_winner(board)
    done=winner!=0 or board_is_full(board)
    return (bool(done),int(winner))

def make_mcts_node(prior=0.0, parent=None):
    #using visits in make node
    return {
        'prior':prior,
        'visits':0,        
        'value_sum':0.0,
        'children':{},
        'parent':parent,
        'is_expanded':False
    }

def backup_value(leaf,value):
    current=leaf
    while current is not None:
        current['visits']+=1
        current['value_sum']+=value
        value=-value
        current=current['parent']

def expand_node(node, priors):
    # TODO: attach a child node for every legal move with the corresponding network prior
    board=node['board']
    player=node['to_play']
    
    for move in valid_moves(board):
        prior=priors[move]
        child=make_mcts_node(prior=float(prior),parent=node)
        
        child['board']=drop_piece(board, move, player)
        child['to_play']=other_player(player)
        
        node['children'][move]=child
        
    node['is_expanded']=True

def evaluate_with_network(net, state, to_play):
    # TODO: run net on encoded state and return (masked priors np.ndarray (7,), value float)
    encoded=encode_board(state, to_play)  
    state_tensor=torch.FloatTensor(encoded).unsqueeze(0) 
    
    with torch.no_grad():
        policy_logits,value_tensor=net(state_tensor)
        
        probs=torch.softmax(policy_logits,dim=1).squeeze(0).numpy()
        value=torch.tanh(value_tensor).item()  
    
    legal_moves=valid_moves(state) 
    mask=np.zeros(7,dtype=np.float32)
    mask[legal_moves]=1.0
    
    masked_priors=probs*mask
    
    sum_priors=np.sum(masked_priors)
    if sum_priors>0:
        masked_priors/=sum_priors
    else:
        masked_priors=mask/np.sum(mask)

    return masked_priors,float(value)

def node_q_value(node):
    # TODO: return the mean value Q = value_sum / visit_count, or 0.0 if visit_count == 0
    if(node['visits']==0):
        return 0.0
    else:
        return node['value_sum']/node['visits']

def ucb_score(parent,child,c_puct=1.5):
    # TODO: return Q(child) + c_puct * prior * sqrt(N_parent) / (1 + N_child)
    return node_q_value(child)+c_puct*child['prior']*math.sqrt(parent['visits'])/(1+child['visits'])

def select_best_child(node, legal_actions, c_puct=1.5):
    # TODO: return (action, child) maximizing PUCT among legal children of node.
    best_score=-float('inf')
    best_action=None
    best_child=None
    
    for action in legal_actions:
        child=node['children'][action]
        score=ucb_score(node,child,c_puct)
        
        if(score>best_score):
            best_score=score
            best_action=action
            best_child=child
            
    return best_action,best_child

def select_leaf(root, c_puct=1.5):
    # TODO: walk down the MCTS tree picking the best PUCT child until a non-expanded node is reached
    current_node=root
    
    while(current_node['children'] is not None and len(current_node['children'])>0):
        legal_actions=list(current_node['children'].keys())
        best_action,best_child=select_best_child(current_node,legal_actions,c_puct)
        current_node=best_child
        
    return current_node   

def run_one_simulation(root, net, c_puct=1.5):
    # TODO: run one MCTS simulation: select a leaf, evaluate, expand if non-terminal, backup.
    leaf=select_leaf(root, c_puct)
    board=leaf['board']
    player=leaf['to_play']
    
    done,winner=is_terminal(board)
    
    if done:
        if winner==player:
            value=1.0
        elif winner==other_player(player):
            value=-1.0
        else:
            value = 0.0
    else:
        priors,value=evaluate_with_network(net,board,player)
        expand_node(leaf,priors)
        
    backup_value(leaf,value)

# Step 36 - run_mcts
import math
import numpy as np
import torch

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # Define helper to check 4 consecutive matching non-zero elements
    def check_line(line):
        for i in range(len(line)-3):
            if line[i]!=0 and line[i]==line[i+1]==line[i+2]==line[i+3]:
                return line[i]
        return 0

    H,W=board.shape

    for row in board:
        winner=check_line(row)
        if winner:return winner

    for col in board.T:
        winner=check_line(col)
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(np.fliplr(board), d))
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(board, d))
        if winner:return winner

    return 0

def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    return 0 not in board[0,:]

def is_terminal(board):
    # TODO: return (done, winner) using check_winner and board_is_full.
    winner=check_winner(board)
    done=winner!=0 or board_is_full(board)
    return (bool(done),int(winner))

def make_mcts_node(prior=0.0, parent=None):
    # Supporting both tracking keys to avoid external harness KeyErrors
    return {
        'prior':prior,
        'visits':0,        
        'visit_count':0,
        'value_sum':0.0,
        'children':{},
        'parent':parent,
        'is_expanded':False
    }

def backup_value(leaf,value):
    current=leaf
    while current is not None:
        current['visits']+=1
        current['visit_count']+=1
        current['value_sum']+=value
        value=-value
        current=current['parent']

def expand_node(node, priors):
    # TODO: attach a child node for every legal move with the corresponding network prior
    board=node['board']
    player=node['to_play']
    
    for move in valid_moves(board):
        prior=priors[move]
        child=make_mcts_node(prior=float(prior),parent=node)
        
        child['board']=drop_piece(board, move, player)
        child['to_play']=other_player(player)
        
        node['children'][move]=child
        
    node['is_expanded']=True

def evaluate_with_network(net, state, to_play):
    # TODO: run net on encoded state and return (masked priors np.ndarray (7,), value float)
    encoded=encode_board(state, to_play)  
    state_tensor=torch.FloatTensor(encoded).unsqueeze(0) 
    
    with torch.no_grad():
        policy_logits,value_tensor=net(state_tensor)
        
        probs=torch.softmax(policy_logits,dim=1).squeeze(0).numpy()
        value=torch.tanh(value_tensor).item()  
    
    legal_moves=valid_moves(state) 
    mask=np.zeros(7,dtype=np.float32)
    mask[legal_moves]=1.0
    
    masked_priors=probs*mask
    
    sum_priors=np.sum(masked_priors)
    if sum_priors>0:
        masked_priors/=sum_priors
    else:
        masked_priors=mask/np.sum(mask)

    return masked_priors,float(value)

def node_q_value(node):
    # Safe check for both naming variants
    v = node['visit_count'] if 'visit_count' in node else node['visits']
    if(v==0):
        return 0.0
    else:
        return node['value_sum']/v

def ucb_score(parent,child,c_puct=1.5):
    p_v = parent['visit_count'] if 'visit_count' in parent else parent['visits']
    c_v = child['visit_count'] if 'visit_count' in child else child['visits']
    return node_q_value(child)+c_puct*child['prior']*math.sqrt(p_v)/(1+c_v)

def select_best_child(node, legal_actions, c_puct=1.5):
    # TODO: return (action, child) maximizing PUCT among legal children of node.
    best_score=-float('inf')
    best_action=None
    best_child=None
    
    for action in legal_actions:
        child=node['children'][action]
        score=ucb_score(node,child,c_puct)
        
        if(score>best_score):
            best_score=score
            best_action=action
            best_child=child
            
    return best_action,best_child

def select_leaf(root, c_puct=1.5):
    # TODO: walk down the MCTS tree picking the best PUCT child until a non-expanded node is reached
    current_node=root
    
    while(current_node['children'] is not None and len(current_node['children'])>0):
        legal_actions=list(current_node['children'].keys())
        best_action,best_child=select_best_child(current_node,legal_actions,c_puct)
        current_node=best_child
        
    return current_node   

def run_one_simulation(root, net, c_puct=1.5):
    # TODO: run one MCTS simulation: select a leaf, evaluate, expand if non-terminal, backup.
    leaf=select_leaf(root, c_puct)
    board=leaf['board']
    player=leaf['to_play']
    
    done, winner = is_terminal(board)
    
    if done:
        if winner == player:
            value = 1.0
        elif winner == other_player(player):
            value = -1.0
        else:
            value = 0.0
    else:
        priors, value = evaluate_with_network(net, board, player)
        expand_node(leaf, priors)
        
    backup_value(leaf, value)

def run_mcts(state, to_play, net, num_simulations, c_puct):
    # TODO: build a fresh root for (state, to_play) and run num_simulations PUCT simulations
    root=make_mcts_node()
    root['board']=state
    root['to_play']=to_play
    root['is_expanded']=False

    for _ in range(num_simulations):
        run_one_simulation(root,net,c_puct)
        
    return root

# Step 37 - visit_count_policy
def visit_count_policy(root, temperature=1.0):
    # TODO: convert root child visit counts into a length-7 probability vector over columns
    counts=np.zeros(7,dtype=np.float64)
    for move,child in root['children'].items():
        counts[move]=child['visit_count']
    
    sum_counts=np.sum(counts)
    if sum_counts==0:
        return np.ones(7,dtype=np.float64)/7.0

    if temperature==0.0:
        best_move=np.argmax(counts)
        policy=np.zeros(7,dtype=np.float64)
        policy[best_move]=1.0
        return policy

    counts=counts**(1.0/temperature)
    sum_counts=np.sum(counts)
    policy=counts/sum_counts

    return policy

# Step 38 - mcts_choose_action
import math
import numpy as np
import torch

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # Define helper to check 4 consecutive matching non-zero elements
    def check_line(line):
        for i in range(len(line)-3):
            if line[i]!=0 and line[i]==line[i+1]==line[i+2]==line[i+3]:
                return line[i]
        return 0

    H,W=board.shape

    for row in board:
        winner=check_line(row)
        if winner:return winner

    for col in board.T:
        winner=check_line(col)
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(np.fliplr(board), d))
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(board, d))
        if winner:return winner

    return 0

def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    return 0 not in board[0,:]

def is_terminal(board):
    # TODO: return (done, winner) using check_winner and board_is_full.
    winner=check_winner(board)
    done=winner!=0 or board_is_full(board)
    return (bool(done),int(winner))

def make_mcts_node(prior=0.0, parent=None):
    # Supporting both tracking keys to avoid external harness KeyErrors
    return {
        'prior':prior,
        'visits':0,        
        'visit_count':0,
        'value_sum':0.0,
        'children':{},
        'parent':parent,
        'is_expanded':False
    }

def backup_value(leaf,value):
    current=leaf
    while current is not None:
        current['visits']+=1
        current['visit_count']+=1
        current['value_sum']+=value
        value=-value
        current=current['parent']

def expand_node(node, priors):
    # TODO: attach a child node for every legal move with the corresponding network prior
    board=node['board']
    player=node['to_play']
    
    for move in valid_moves(board):
        prior=priors[move]
        child=make_mcts_node(prior=float(prior),parent=node)
        
        child['board']=drop_piece(board, move, player)
        child['to_play']=other_player(player)
        
        node['children'][move]=child
        
    node['is_expanded']=True

def evaluate_with_network(net, state, to_play):
    # TODO: run net on encoded state and return (masked priors np.ndarray (7,), value float)
    encoded=encode_board(state, to_play)  
    state_tensor=torch.FloatTensor(encoded).unsqueeze(0) 
    
    with torch.no_grad():
        policy_logits,value_tensor=net(state_tensor)
        
        probs=torch.softmax(policy_logits,dim=1).squeeze(0).numpy()
        value=torch.tanh(value_tensor).item()  
    
    legal_moves=valid_moves(state) 
    mask=np.zeros(7,dtype=np.float32)
    mask[legal_moves]=1.0
    
    masked_priors=probs*mask
    
    sum_priors=np.sum(masked_priors)
    if sum_priors>0:
        masked_priors/=sum_priors
    else:
        masked_priors=mask/np.sum(mask)

    return masked_priors,float(value)

def node_q_value(node):
    # Safe check for both naming variants
    v = node['visit_count'] if 'visit_count' in node else node['visits']
    if(v==0):
        return 0.0
    else:
        return node['value_sum']/v

def ucb_score(parent,child,c_puct=1.5):
    p_v = parent['visit_count'] if 'visit_count' in parent else parent['visits']
    c_v = child['visit_count'] if 'visit_count' in child else child['visits']
    return node_q_value(child)+c_puct*child['prior']*math.sqrt(p_v)/(1+c_v)

def select_best_child(node, legal_actions, c_puct=1.5):
    # TODO: return (action, child) maximizing PUCT among legal children of node.
    best_score=-float('inf')
    best_action=None
    best_child=None
    
    for action in legal_actions:
        child=node['children'][action]
        score=ucb_score(node,child,c_puct)
        
        if(score>best_score):
            best_score=score
            best_action=action
            best_child=child
            
    return best_action,best_child

def select_leaf(root, c_puct=1.5):
    # TODO: walk down the MCTS tree picking the best PUCT child until a non-expanded node is reached
    current_node=root
    
    while(current_node['is_expanded'] and len(current_node['children'])>0):
        legal_actions=list(current_node['children'].keys())
        best_action,best_child=select_best_child(current_node,legal_actions,c_puct)
        current_node=best_child
        
    return current_node   

def run_one_simulation(root, net, c_puct=1.5):
    # TODO: run one MCTS simulation: select a leaf, evaluate, expand if non-terminal, backup.
    leaf=select_leaf(root, c_puct)
    board=leaf['board']
    player=leaf['to_play']
    
    done, winner = is_terminal(board)
    
    if done:
        if winner == player:
            value = 1.0
        elif winner == other_player(player):
            value = -1.0
        else:
            value = 0.0
    else:
        priors, value = evaluate_with_network(net, board, player)
        expand_node(leaf, priors)
        
    backup_value(leaf, value)

def run_mcts(state, to_play, net, num_simulations, c_puct):
    # TODO: build a fresh root for (state, to_play) and run num_simulations PUCT simulations
    root=make_mcts_node()
    root['board']=state
    root['to_play']=to_play
    root['is_expanded']=False

    # AlphaZero expands the root immediately before running targeted tree simulations
    priors, value = evaluate_with_network(net, state, to_play)
    expand_node(root, priors)

    for _ in range(num_simulations):
        run_one_simulation(root,net,c_puct)
        
    return root

def mcts_choose_action(state, to_play, net, num_simulations, c_puct, temperature=1.0):
    # TODO: Run MCTS at the given state and return (action, visit-count policy vector).
    root=run_mcts(state,to_play,net,num_simulations,c_puct)
    
    counts=np.zeros(7,dtype=np.float32)
    for move,child in root['children'].items():
        counts[move]=child['visit_count']
        
    if temperature==0.0:
        action=int(np.argmax(counts))
        policy=np.zeros(7,dtype=np.float32)
        policy[action]=1.0
        return action,policy
        
    counts=counts**(1.0/temperature)
    sum_counts=np.sum(counts)
    policy=counts/sum_counts
    
    action=int(torch.multinomial(torch.FloatTensor(policy), 1).item())
    return action,policy

# Step 39 - record_self_play_step
def record_self_play_step(history, board, policy, to_play):
    # TODO: append a dict with 'board', 'policy', 'to_play' to history and return history
    history.append({'board':board.copy(),'policy':policy.copy(),'to_play':to_play})
    return history

# Step 40 - play_self_play_game
import math
import numpy as np
import torch
import copy

def check_winner(board):
    def check_line(line):
        for i in range(len(line)-3):
            if line[i]!=0 and line[i]==line[i+1]==line[i+2]==line[i+3]:
                return line[i]
        return 0

    H,W=board.shape

    for row in board:
        winner=check_line(row)
        if winner:return winner

    for col in board.T:
        winner=check_line(col)
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(np.fliplr(board), d))
        if winner:return winner

    for d in range(-H+4,W-3):
        winner=check_line(np.diag(board, d))
        if winner:return winner

    return 0

def board_is_full(board):
    return 0 not in board[0,:]

def is_terminal(board):
    winner=check_winner(board)
    done=winner!=0 or board_is_full(board)
    return (bool(done),int(winner))

def drop_piece(board, column, player):
    board_copy=copy.deepcopy(board)
    for row in range(len(board_copy)-1, -1, -1):
        if board_copy[row][column]==0:
            board_copy[row][column]=player
            break
    else:
        raise ValueError("")
    return board_copy

def step_env(board, column, player):
    new_board=drop_piece(board,column,player)
    t=is_terminal(new_board)
    done=t[0]
    winner=t[1]
    next_player=2 if player==1 else 1
    return (new_board, done, winner, next_player)

def valid_moves(board):
    return [col for col in range(len(board[0])) if any(board[row][col]==0 for row in range(len(board)))]

def other_player(player):
    if player==1:
        return 2
    return 1

def encode_board(board, current_player):
    opponent=3-current_player
    channel1=(board==current_player).astype(np.float32)
    channel2=(board==opponent).astype(np.float32)
    return np.stack([channel1,channel2],axis=0)

def make_mcts_node(prior=0.0, parent=None):
    return {
        'prior':float(prior),
        'visits':0,
        'visit_count':0,
        'value_sum':0.0,
        'children':{},
        'parent':parent,
        'is_expanded':False
    }

def backup_value(leaf, value):
    current=leaf
    while current is not None:
        current['visits']+=1
        current['visit_count']+=1
        current['value_sum']+=float(value)
        value=-float(value)
        current=current['parent']

def expand_node(node, priors):
    board=node['board']
    player=node['to_play']
    for move in valid_moves(board):
        prior=float(priors[move])
        child=make_mcts_node(prior=prior, parent=node)
        child['board']=drop_piece(board, move, player)
        child['to_play']=other_player(player)
        node['children'][move]=child
    node['is_expanded']=True

def evaluate_with_network(net, state, to_play):
    encoded=encode_board(state, to_play)
    state_tensor=torch.FloatTensor(encoded).unsqueeze(0)

    with torch.no_grad():
        output=net(state_tensor)
        if isinstance(output, (tuple, list)):
            policy_logits=output[0]
            value_tensor=output[1]
        else:
            policy_logits=output
            value_tensor=torch.zeros(1)

        probs=torch.softmax(policy_logits,dim=1).squeeze(0).numpy()
        value=float(torch.tanh(value_tensor).squeeze())

    legal_moves=valid_moves(state)
    mask=np.zeros(7,dtype=np.float32)
    mask[legal_moves]=1.0

    masked_priors=probs*mask
    sum_priors=float(np.sum(masked_priors))
    if sum_priors>0:
        masked_priors=masked_priors/sum_priors
    else:
        masked_priors=mask/float(np.sum(mask))

    return masked_priors, value

def node_q_value(node):
    v=node['visit_count']
    if v==0:
        return 0.0
    return node['value_sum']/float(v)

def ucb_score(parent, child, c_puct=1.5):
    p_v=float(parent['visit_count'])
    c_v=float(child['visit_count'])
    q=node_q_value(child)
    u=c_puct*float(child['prior'])*math.sqrt(p_v)/(1.0+c_v)
    return q+u

def select_best_child(node, legal_actions, c_puct=1.5):
    best_score=-float('inf')
    best_action=None
    best_child=None
    for action in legal_actions:
        child=node['children'][action]
        score=ucb_score(node,child,c_puct)
        if score>best_score:
            best_score=score
            best_action=action
            best_child=child
    return best_action, best_child

def select_leaf(root, c_puct=1.5):
    current=root
    while current['is_expanded'] and len(current['children'])>0:
        legal_actions=list(current['children'].keys())
        r=select_best_child(current,legal_actions,c_puct)
        current=r[1]
    return current

def run_one_simulation(root, net, c_puct=1.5):
    leaf=select_leaf(root, c_puct)
    board=leaf['board']
    player=leaf['to_play']

    t=is_terminal(board)
    done=t[0]
    winner=t[1]

    if done:
        if winner==player:
            value=1.0
        elif winner==other_player(player):
            value=-1.0
        else:
            value=0.0
    else:
        r=evaluate_with_network(net, board, player)
        priors=r[0]
        value=r[1]
        expand_node(leaf, priors)

    backup_value(leaf, value)

def run_mcts(state, to_play, net, num_simulations, c_puct):
    root=make_mcts_node()
    root['board']=state.copy()
    root['to_play']=to_play
    root['is_expanded']=False

    r=evaluate_with_network(net, state, to_play)
    priors=r[0]
    expand_node(root, priors)

    for _ in range(num_simulations):
        run_one_simulation(root, net, c_puct)

    return root

def mcts_choose_action(state, to_play, net, num_simulations, c_puct, temperature=1.0):
    root=run_mcts(state, to_play, net, num_simulations, c_puct)

    counts=np.zeros(7, dtype=np.float64)
    for move in root['children']:
        counts[move]=float(root['children'][move]['visit_count'])

    if temperature==0.0:
        action=int(np.argmax(counts))
        policy=np.zeros(7, dtype=np.float64)
        policy[action]=1.0
        return action, policy

    counts=counts**(1.0/temperature)
    total=float(np.sum(counts))
    if total>0:
        policy=counts/total
    else:
        policy=np.ones(7, dtype=np.float64)/7.0

    action=int(torch.multinomial(torch.FloatTensor(policy.astype(np.float32)),1).item())
    return action, policy

def record_self_play_step(board, policy, to_play):
    return {
        'board': board.copy(),
        'policy': policy,
        'to_play': to_play
    }

def play_self_play_game(net, num_simulations, c_puct, temperature=1.0):
    board=np.zeros((6,7), dtype=np.int8)
    player=1
    history=[]

    while True:
        r=mcts_choose_action(board, player, net, num_simulations, c_puct, temperature)
        action=int(r[0])
        policy=r[1]

        history.append(record_self_play_step(board, policy, player))

        s=step_env(board, action, player)
        board=s[0]
        done=s[1]
        winner=s[2]
        player=s[3]

        if done:
            break

    return history, winner

# Step 41 - assign_value_targets
def assign_value_targets(history, winner):
    # TODO: return a new list of step dicts each annotated with a 'value' target in {-1.0, 0.0, 1.0}.
    annotated_history=[]
    
    for step in history:
        new_step=step.copy()
        if winner==0:
            new_step['value']=0.0
        elif step['to_play']==winner:
            new_step['value']=1.0
        else:
            new_step['value']=-1.0
            
        annotated_history.append(new_step)
        
    return annotated_history

# Step 42 - generate_self_play_batch
import numpy as np

def generate_self_play_batch(net, num_games, num_simulations, c_puct, temperature=1.0):
    ans = []

    for _ in range(num_games):
        history, winner = play_self_play_game(net, num_simulations, c_puct, temperature)

        for step in history:
            state = step['board']
            policy = step['policy']
            to_play = step['to_play']

            value = 0.0 if winner == 0 else (1.0 if winner == to_play else -1.0)
            board_2d = np.asarray(state)
            policy_1d = np.asarray(policy).flatten()

            ans.append({
                'board': board_2d,
                'policy': policy_1d,
                'to_play': to_play,
                'value': value
            })

    return ans

# Step 43 - value_loss_mse
import torch

def value_loss_mse(predicted_values, target_values):
    # TODO: return the mean squared error between predicted and target values
    return torch.mean((predicted_values-target_values)**2)

# Step 44 - policy_loss_cross_entropy
import torch

def policy_loss_cross_entropy(predicted_log_probs, target_policy):
    """Cross-entropy between MCTS target policy and network log-probs. Returns scalar tensor."""
    # TODO: compute -sum(target * log_probs) per row, then average over the batch
    return -torch.mean(torch.sum(target_policy*predicted_log_probs,dim=-1))

# Step 45 - l2_regularization_loss
def l2_regularization_loss(net):
    # TODO: return the sum of squared L2 norms of all trainable parameters in net
    losses=[torch.sum(p**2) for p in net.parameters() if p.requires_grad]
    return sum(losses) if losses else torch.tensor(0.0,requires_grad=True)

# Step 46 - combined_loss (not yet solved)
# TODO: implement

# Step 47 - encode_batch_states (not yet solved)
# TODO: implement

# Step 48 - iterate_minibatches (not yet solved)
# TODO: implement

# Step 49 - training_step (not yet solved)
# TODO: implement

# Step 50 - training_epoch (not yet solved)
# TODO: implement

# Step 51 - self_play_iteration (not yet solved)
# TODO: implement

# Step 52 - train_loop (not yet solved)
# TODO: implement

# Step 53 - random_policy_action (not yet solved)
# TODO: implement

# Step 54 - greedy_agent_action (not yet solved)
# TODO: implement

# Step 55 - play_one_match (not yet solved)
# TODO: implement

# Step 56 - match_win_rate (not yet solved)
# TODO: implement

# Step 57 - evaluate_against_random (not yet solved)
# TODO: implement

