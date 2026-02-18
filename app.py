import streamlit as st
import pandas as pd
from sklearn . m o d e l _ s e l e c t i o n import t r a i n _ t e s t _ s p l i t
from sklearn . f e a t u r e _ e x t r a c t i o n . text import T f i d f V e c t o r i z e r
from sklearn . n a i v e _ b a y e s import M u l t i n o m i a l N B
from sklearn . metrics import accuracy_score , c o n f u s i o n _ m a t r i x
import seaborn as sns
import m at pl ot li b . pyplot as plt
st . title ( " IMDB Sentiment Analysis " )
u p l o a d e d _ f i l e = st . f i l e _ u p l o a d e r ( " Upload IMDB Dataset CSV "
, type = " csv " )
if u p l o a d e d _ f i l e :
df = pd . read_csv ( u p l o a d e d _ f i l e )
df [ ’ sentiment ’] = df [ ’ sentiment ’ ]. map ({ ’ positive ’: 1 , ’ negative ’: 0})
st . write ( df . head () )
X_train , X_test , y_train , y_test = t r a i n _ t e s t _ s p l i t ( df [ ’ review ’] , df [ ’
sentiment ’] , test_size =0.2 , r a n d o m _ s t a t e =42)
tfidf = T f i d f V e c t o r i z e r ( st op _w or ds = ’ english ’ , m a x _ f e a t u r e s =5000)
X _ t r a i n _ t f i d f = tfidf . f i t _ t r a n s f o r m ( X_train )
X _ t e s t _ t f i d f = tfidf . transform ( X_test )
nb = M u l t i n o m i a l N B ()
nb . fit ( X_train_tfidf , y_train )
y_pred = nb . predict ( X _ t e s t _ t f i d f )
st . write ( f " Accuracy : { a c c u r a c y _ s c o r e ( y_test , y_pred ) :.4 f } " )
fig , ax = plt . subplots ()
sns . heatmap ( c o n f u s i o n _ m a t r i x ( y_test , y_pred ) , annot = True , fmt = ’d ’ , cmap = ’
mako ’ , ax = ax )
ax . set_title ( " Sentiment Analysis Confusion Matrix " )
st . pyplot ( fig )
u s e r _ r e v i e w = st . t ex t_i np ut ( " Test a Review " )
if u s e r _ r e v i e w :
vec = tfidf . transform ([ u s e r _ r e v i e w ])
st . write ( f " Sentiment : { ’ Positive ’ if nb . predict ( vec ) [0] == 1 else ’
Negative ’} " )
