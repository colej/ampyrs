import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams.update({
    "text.usetex": True,
        "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})
plt.rcParams.update({
    "pgf.rcfonts": False,
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": "\n".join([
         r"\usepackage{amsmath}",
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
    ]),
})

plt.rcParams['xtick.labelsize']=18
plt.rcParams['ytick.labelsize']=18


if __name__ == '__main__':


    tess_wvl, tess_rsp = np.loadtxt('../data/transmission_functions/TESS_TESS.Red.dat').T
    df = pd.read_csv('../data/transmission_functions/bg_filters.csv')
    # gaiaR_wvl, gaiaR_rsp = np.loadtxt('./transmission_functions/GAIA_GAIA3.Grp.dat').T
    # gaiaB_wvl, gaiaB_rsp = np.loadtxt('./transmission_functions/GAIA_GAIA3.Gbp.dat').T
    gaiaG_wvl, gaiaG_rsp = np.loadtxt('../data/transmission_functions/GAIA_GAIA3.G.dat').T

    colors = ['dodgerblue', 'forestgreen', 'goldenrod', 'firebrick','rebeccapurple', 'darkorange']
    fig, ax = plt.subplots(1,1,figsize=(6.69,6.69), dpi=250)

    ax.plot(tess_wvl, 100*tess_rsp, '--', color='dimgrey')
    ax.fill_between(tess_wvl, y1=0, y2=100*tess_rsp, facecolor='None', hatch='//', alpha=0.5, label=r'${\it TESS}$' )
    # ax.plot(gaiaR_wvl, gaiaR_rsp, 'r--', alpha=0.5)
    # ax.plot(gaiaB_wvl, gaiaB_rsp, 'b--', alpha=0.5)
    ax.plot(gaiaG_wvl, 100*gaiaG_rsp, 'b:', alpha=0.7)
    ax.fill_between(gaiaG_wvl, y1=0, y2=100*gaiaG_rsp, facecolor='None', hatch='\\', alpha=0.5, label=r'${\it Gaia~G}$' )

    for ii, fltr in enumerate(['u','g','r','i','z','q']):

        dfx = df.loc[( (df['transmission_{}'.format(fltr)]>0.01) & (df.wavelength < 1010) )]
        ax.plot(df.wavelength*10, df['transmission_{}'.format(fltr)], color=colors[ii], )
        ax.fill_between(dfx.wavelength*10, y1=0, y2=dfx['transmission_{}'.format(fltr)], color=colors[ii], alpha=0.4, label=r'{}'.format(fltr) )
        print('{} filter mean'.format(fltr), np.mean(dfx.wavelength))


    ax.set_xlabel(r'${\rm Wavelength~[\AA]}$', fontsize=18)
    ax.set_ylabel(r'${\rm Transmission}$', fontsize=18)
    ax.set_ylim(0.,105.)

    ax.legend(loc='upper right')
    fig.tight_layout()
    fig.savefig('../figures/filter_transmission_v02.png')
    plt.show()
