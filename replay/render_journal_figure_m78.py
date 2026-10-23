"""Grayscale/hatch publication figure from captured CSVs; optional matplotlib."""
import argparse
import csv
from pathlib import Path
import tempfile

import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='maestro-x-m78-grayscale'
matplotlib.rcParams.update({'font.size':13,'axes.titlesize':14,'axes.labelsize':13,
    'xtick.labelsize':12,'ytick.labelsize':12})
import matplotlib.pyplot as plt


def build(data,output):
    with (data/'conditions.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    with (data/'sensitivity.csv').open(encoding='utf-8',newline='') as f:grid=list(csv.DictReader(f))
    fig,axes=plt.subplots(1,3,figsize=(12,3.5),layout='constrained')
    votes=('ACCEPT','REJECT','ABSTAIN','FAILED');shades=('#eeeeee','#555555','#aaaaaa','#111111')
    patterns=('','///','xx','...');x=list(range(4));bottom=[0]*4
    for vote,shade,hatch in zip(votes,shades,patterns):
        values=[int(r[vote]) for r in rows]
        axes[0].bar(x,values,bottom=bottom,label=vote,color=shade,hatch=hatch,edgecolor='black',linewidth=.4)
        bottom=[a+b for a,b in zip(bottom,values)]
    axes[0].set(xticks=x,xticklabels=[r['condition'] for r in rows],ylabel='Cases',ylim=(0,42),title='Decisions')
    axes[0].legend(fontsize=13)
    known=[int(r['known_invalid_ACCEPT']) for r in rows];unknown=[int(r['unknown_label_ACCEPT']) for r in rows]
    axes[1].bar(x,known,label='Known invalid',color='#555555',hatch='///',edgecolor='black',linewidth=.4)
    axes[1].bar(x,unknown,bottom=known,label='Unknown label',color='#cccccc',hatch='xx',edgecolor='black',linewidth=.4)
    axes[1].set(xticks=x,xticklabels=[r['condition'] for r in rows],ylabel='Accepted cases',ylim=(0,42),title='Action audit');axes[1].legend(fontsize=13)
    for vote,line,marker in zip(votes,('-','--',':','-.'),('o','s','^','x')):
        if vote=='FAILED':continue
        axes[2].plot([int(r['cap_percent']) for r in grid],[int(r[vote]) for r in grid],label=vote,color='black',linestyle=line,marker=marker,linewidth=1.4,markersize=4)
    axes[2].set(xlabel='Cash-risk cap (%)',ylabel='Cases',xticks=[1,2,3,4,5],ylim=(0,42),title='Guard sensitivity');axes[2].legend(fontsize=13)
    for ax in axes:ax.spines[['top','right']].set_visible(False)
    fig.savefig(output/'journal-results.png',dpi=240,metadata={'Software':'Maestro-X M78'})
    fig.savefig(output/'journal-results.svg',metadata={'Date':None});plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',type=Path,default=Path(__file__).resolve().parent);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    a.out.mkdir();build(a.data,a.out)
    with tempfile.TemporaryDirectory(prefix='mx-m78-plot-') as tmp:
        other=Path(tmp);build(a.data,other)
        for f in a.out.iterdir():
            if f.read_bytes()!=(other/f.name).read_bytes():raise ValueError('Figure build differs')
    print('PASS_GRAYSCALE_FIGURES_TWO_BYTE_IDENTICAL_RENDERS')
