from numpy import random
import time
def extract_comments(links, n_links=None, rs=42, verbose=True):
    """
    The functions extract the text data from random subst of a given number of links
    links: an iterable with links, e.g a list or a pandas series
    n_links: the number of randomly selected links
    rs: random state
    verbose: if True the links are printed to the console
    """
    if rs is not None:
        random.seed(rs)
    if n_links is None:
        n_links = len(links)
    random_links = random.choice(links,  n_links, replace=False)
    
    random.seed()
    r = random.random()
    time.sleep(r)
    
    comments = []
    for e, link in enumerate(random_links):
        if verbose:
            print(f'Processing link {e+1} from {n_links}: {link}')
            
        txt = text_exctraction(link)
        cleaned_txt = clean_text(txt, ['\n', 'Schließen', '\r'])
        if cleaned_txt is not None:
            comments.append(cleaned_txt)
        
    return ' '.join(set(comments))
