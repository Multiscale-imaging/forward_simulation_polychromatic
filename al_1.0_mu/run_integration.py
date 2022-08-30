import dfxm_fwrd_sim.parameter_parser as par
import dfxm_fwrd_sim.integrate as integrate
import sys

phi = float(sys.argv[1])*1e-6
print(phi)

par_fn = '/u/data/madsac/Foward_simulation_polychromatic/al_1.0_mu/al_1.ini'
params = par.par_read(par_fn)
params['Status']['processes'] = 11
par.par_write(params) 
integrate.integrate_parallel(par_fn, phi)
