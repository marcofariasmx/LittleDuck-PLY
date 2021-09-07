
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA CTEF CTEI CTESTRING DIVIDE ELSE EQUALS FLOAT GREATER ID IF INT LEFTBRACKET LEFTPAREN LESS MINUS NOTEQUAL PLUS PRINT PROGRAM RIGHTBRACKET RIGHTPAREN SEMICOLON TIMES VARprogram : PROGRAM ID SEMICOLON program_vars blockprogram_vars : vars\n               | emptyblock : LEFTBRACKET statement_block RIGHTBRACKETstatement_block : statement statement_block\n                       | emptystatement : assignment\n                 | condition\n                 | writingexpression : exp comparationcomparation : GREATER comparation_exp\n                      | LESS comparation_exp\n                      | NOTEQUAL comparation_exp\n                      | emptycomparation_exp : expexp : term operatoroperator : PLUS term operator\n                | MINUS term operator\n                | emptyterm : factor term_operatorterm_operator : TIMES factor term_operator\n                     | DIVIDE factor term_operator\n                     | emptyfactor : LEFTPAREN expression RIGHTPAREN\n              | sign var_ctesign : PLUS\n            | MINUS\n            | emptyvar_cte : ID\n               | CTEI\n               | CTEFvars : VAR var_id COLON type SEMICOLON vars_blockvar_id : ID var_id_2var_id_2 : COMMA ID var_id_2\n                | emptytype : INT\n            | FLOATvars_block : var_id COLON type SEMICOLON vars_block\n                  | emptyassignment : ID EQUALS expression SEMICOLONcondition : IF LEFTPAREN expression RIGHTPAREN block else_condition SEMICOLONelse_condition : ELSE block\n                      | emptywriting : PRINT LEFTPAREN print_val RIGHTPAREN SEMICOLONprint_val : expression print_exp\n                 | CTESTRING print_expprint_exp : COMMA  print_val\n                 | emptyempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,9,26,],[0,-1,-4,]),'ID':([2,8,10,14,16,17,18,24,28,29,30,39,40,41,42,43,48,50,52,53,54,57,58,61,62,72,88,99,101,],[3,12,19,19,-7,-8,-9,34,-49,-49,-49,-49,66,-26,-27,-28,12,-40,-49,-49,-49,-49,-49,-49,-49,-49,-44,-41,12,]),'SEMICOLON':([3,26,31,32,33,35,36,37,38,51,55,56,59,60,63,65,66,67,68,70,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,97,98,100,],[4,-4,48,-36,-37,50,-49,-49,-49,-10,-14,-16,-19,-20,-23,-25,-29,-30,-31,88,-11,-15,-12,-13,-49,-49,-49,-49,-24,-49,-17,-18,-21,-22,99,-43,101,-42,]),'VAR':([4,],[8,]),'LEFTBRACKET':([4,5,6,7,48,69,76,77,96,101,102,],[-49,10,-2,-3,-49,10,-32,-39,10,-49,-38,]),'RIGHTBRACKET':([10,13,14,15,16,17,18,27,50,88,99,],[-49,26,-49,-6,-7,-8,-9,-5,-40,-44,-41,]),'IF':([10,14,16,17,18,50,88,99,],[20,20,-7,-8,-9,-40,-44,-41,]),'PRINT':([10,14,16,17,18,50,88,99,],[21,21,-7,-8,-9,-40,-44,-41,]),'COLON':([11,12,23,25,34,49,75,],[22,-49,-33,-35,-49,-34,90,]),'COMMA':([12,34,36,37,38,46,47,51,55,56,59,60,63,65,66,67,68,78,79,80,81,82,83,84,85,86,91,92,93,94,],[24,24,-49,-49,-49,72,72,-10,-14,-16,-19,-20,-23,-25,-29,-30,-31,-11,-15,-12,-13,-49,-49,-49,-49,-24,-17,-18,-21,-22,]),'EQUALS':([19,],[28,]),'LEFTPAREN':([20,21,28,29,30,39,52,53,54,57,58,61,62,72,],[29,30,39,39,39,39,39,39,39,39,39,39,39,39,]),'INT':([22,90,],[32,32,]),'FLOAT':([22,90,],[33,33,]),'ELSE':([26,87,],[-4,96,]),'PLUS':([28,29,30,37,38,39,52,53,54,57,58,60,61,62,63,65,66,67,68,72,82,83,84,85,86,93,94,],[41,41,41,57,-49,41,41,41,41,41,41,-20,41,41,-23,-25,-29,-30,-31,41,57,57,-49,-49,-24,-21,-22,]),'MINUS':([28,29,30,37,38,39,52,53,54,57,58,60,61,62,63,65,66,67,68,72,82,83,84,85,86,93,94,],[42,42,42,58,-49,42,42,42,42,42,42,-20,42,42,-23,-25,-29,-30,-31,42,58,58,-49,-49,-24,-21,-22,]),'CTEI':([28,29,30,39,40,41,42,43,52,53,54,57,58,61,62,72,],[-49,-49,-49,-49,67,-26,-27,-28,-49,-49,-49,-49,-49,-49,-49,-49,]),'CTEF':([28,29,30,39,40,41,42,43,52,53,54,57,58,61,62,72,],[-49,-49,-49,-49,68,-26,-27,-28,-49,-49,-49,-49,-49,-49,-49,-49,]),'CTESTRING':([30,72,],[47,47,]),'GREATER':([36,37,38,56,59,60,63,65,66,67,68,82,83,84,85,86,91,92,93,94,],[52,-49,-49,-16,-19,-20,-23,-25,-29,-30,-31,-49,-49,-49,-49,-24,-17,-18,-21,-22,]),'LESS':([36,37,38,56,59,60,63,65,66,67,68,82,83,84,85,86,91,92,93,94,],[53,-49,-49,-16,-19,-20,-23,-25,-29,-30,-31,-49,-49,-49,-49,-24,-17,-18,-21,-22,]),'NOTEQUAL':([36,37,38,56,59,60,63,65,66,67,68,82,83,84,85,86,91,92,93,94,],[54,-49,-49,-16,-19,-20,-23,-25,-29,-30,-31,-49,-49,-49,-49,-24,-17,-18,-21,-22,]),'RIGHTPAREN':([36,37,38,44,45,46,47,51,55,56,59,60,63,64,65,66,67,68,71,73,74,78,79,80,81,82,83,84,85,86,89,91,92,93,94,],[-49,-49,-49,69,70,-49,-49,-10,-14,-16,-19,-20,-23,86,-25,-29,-30,-31,-45,-48,-46,-11,-15,-12,-13,-49,-49,-49,-49,-24,-47,-17,-18,-21,-22,]),'TIMES':([38,65,66,67,68,84,85,86,],[61,-25,-29,-30,-31,61,61,-24,]),'DIVIDE':([38,65,66,67,68,84,85,86,],[62,-25,-29,-30,-31,62,62,-24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_vars':([4,],[5,]),'vars':([4,],[6,]),'empty':([4,10,12,14,28,29,30,34,36,37,38,39,46,47,48,52,53,54,57,58,61,62,72,82,83,84,85,87,101,],[7,15,25,15,43,43,43,25,55,59,63,43,73,73,77,43,43,43,43,43,43,43,43,59,59,63,63,97,77,]),'block':([5,69,96,],[9,87,100,]),'var_id':([8,48,101,],[11,75,75,]),'statement_block':([10,14,],[13,27,]),'statement':([10,14,],[14,14,]),'assignment':([10,14,],[16,16,]),'condition':([10,14,],[17,17,]),'writing':([10,14,],[18,18,]),'var_id_2':([12,34,],[23,49,]),'type':([22,90,],[31,98,]),'expression':([28,29,30,39,72,],[35,44,46,64,46,]),'exp':([28,29,30,39,52,53,54,72,],[36,36,36,36,79,79,79,36,]),'term':([28,29,30,39,52,53,54,57,58,72,],[37,37,37,37,37,37,37,82,83,37,]),'factor':([28,29,30,39,52,53,54,57,58,61,62,72,],[38,38,38,38,38,38,38,38,38,84,85,38,]),'sign':([28,29,30,39,52,53,54,57,58,61,62,72,],[40,40,40,40,40,40,40,40,40,40,40,40,]),'print_val':([30,72,],[45,89,]),'comparation':([36,],[51,]),'operator':([37,82,83,],[56,91,92,]),'term_operator':([38,84,85,],[60,93,94,]),'var_cte':([40,],[65,]),'print_exp':([46,47,],[71,74,]),'vars_block':([48,101,],[76,102,]),'comparation_exp':([52,53,54,],[78,80,81,]),'else_condition':([87,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON program_vars block','program',5,'p_program','yacc-parser.py',4),
  ('program_vars -> vars','program_vars',1,'p_program_vars','yacc-parser.py',9),
  ('program_vars -> empty','program_vars',1,'p_program_vars','yacc-parser.py',10),
  ('block -> LEFTBRACKET statement_block RIGHTBRACKET','block',3,'p_block','yacc-parser.py',14),
  ('statement_block -> statement statement_block','statement_block',2,'p_statement_block','yacc-parser.py',18),
  ('statement_block -> empty','statement_block',1,'p_statement_block','yacc-parser.py',19),
  ('statement -> assignment','statement',1,'p_statement','yacc-parser.py',23),
  ('statement -> condition','statement',1,'p_statement','yacc-parser.py',24),
  ('statement -> writing','statement',1,'p_statement','yacc-parser.py',25),
  ('expression -> exp comparation','expression',2,'p_expression','yacc-parser.py',29),
  ('comparation -> GREATER comparation_exp','comparation',2,'p_comparation','yacc-parser.py',33),
  ('comparation -> LESS comparation_exp','comparation',2,'p_comparation','yacc-parser.py',34),
  ('comparation -> NOTEQUAL comparation_exp','comparation',2,'p_comparation','yacc-parser.py',35),
  ('comparation -> empty','comparation',1,'p_comparation','yacc-parser.py',36),
  ('comparation_exp -> exp','comparation_exp',1,'p_comparation_exp','yacc-parser.py',40),
  ('exp -> term operator','exp',2,'p_exp','yacc-parser.py',44),
  ('operator -> PLUS term operator','operator',3,'p_operator','yacc-parser.py',48),
  ('operator -> MINUS term operator','operator',3,'p_operator','yacc-parser.py',49),
  ('operator -> empty','operator',1,'p_operator','yacc-parser.py',50),
  ('term -> factor term_operator','term',2,'p_term','yacc-parser.py',54),
  ('term_operator -> TIMES factor term_operator','term_operator',3,'p_term_operator','yacc-parser.py',58),
  ('term_operator -> DIVIDE factor term_operator','term_operator',3,'p_term_operator','yacc-parser.py',59),
  ('term_operator -> empty','term_operator',1,'p_term_operator','yacc-parser.py',60),
  ('factor -> LEFTPAREN expression RIGHTPAREN','factor',3,'p_factor','yacc-parser.py',64),
  ('factor -> sign var_cte','factor',2,'p_factor','yacc-parser.py',65),
  ('sign -> PLUS','sign',1,'p_sing','yacc-parser.py',69),
  ('sign -> MINUS','sign',1,'p_sing','yacc-parser.py',70),
  ('sign -> empty','sign',1,'p_sing','yacc-parser.py',71),
  ('var_cte -> ID','var_cte',1,'p_var_cte','yacc-parser.py',75),
  ('var_cte -> CTEI','var_cte',1,'p_var_cte','yacc-parser.py',76),
  ('var_cte -> CTEF','var_cte',1,'p_var_cte','yacc-parser.py',77),
  ('vars -> VAR var_id COLON type SEMICOLON vars_block','vars',6,'p_vars','yacc-parser.py',81),
  ('var_id -> ID var_id_2','var_id',2,'p_var_id','yacc-parser.py',85),
  ('var_id_2 -> COMMA ID var_id_2','var_id_2',3,'p_var_id_2','yacc-parser.py',89),
  ('var_id_2 -> empty','var_id_2',1,'p_var_id_2','yacc-parser.py',90),
  ('type -> INT','type',1,'p_type','yacc-parser.py',94),
  ('type -> FLOAT','type',1,'p_type','yacc-parser.py',95),
  ('vars_block -> var_id COLON type SEMICOLON vars_block','vars_block',5,'p_vars_block','yacc-parser.py',99),
  ('vars_block -> empty','vars_block',1,'p_vars_block','yacc-parser.py',100),
  ('assignment -> ID EQUALS expression SEMICOLON','assignment',4,'p_assignment','yacc-parser.py',104),
  ('condition -> IF LEFTPAREN expression RIGHTPAREN block else_condition SEMICOLON','condition',7,'p_condition','yacc-parser.py',108),
  ('else_condition -> ELSE block','else_condition',2,'p_else_condition','yacc-parser.py',112),
  ('else_condition -> empty','else_condition',1,'p_else_condition','yacc-parser.py',113),
  ('writing -> PRINT LEFTPAREN print_val RIGHTPAREN SEMICOLON','writing',5,'p_writing','yacc-parser.py',117),
  ('print_val -> expression print_exp','print_val',2,'p_print_val','yacc-parser.py',121),
  ('print_val -> CTESTRING print_exp','print_val',2,'p_print_val','yacc-parser.py',122),
  ('print_exp -> COMMA print_val','print_exp',2,'p_print_exp','yacc-parser.py',126),
  ('print_exp -> empty','print_exp',1,'p_print_exp','yacc-parser.py',127),
  ('empty -> <empty>','empty',0,'p_empty','yacc-parser.py',137),
]
