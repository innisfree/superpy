# SuperPy: Jacobian for naturalness priors.
# J = 7.71064894e+06
# b = 8.74646419e+04
# Mu = 9.11876000e+01
# SOFTSUSY3.4.0 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
# B.C. Allanach and M.A. Bernhardt, Comput. Phys. Commun. 181 (2010) 232,
# arXiv:0903.1805
# B.C. Allanach, M. Hanussek and C.H. Kom, arXiv:1109.3735
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.0       # version number
Block MODSEL  # Select model
     1    1   # sugra
     4    1   # R-parity violating
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
    21    4.75000000e-03   # Mdown(2 GeV) MSbar
    22    2.40000000e-03   # Mup(2 GeV) MSbar
    23    1.04000000e-01   # Mstrange(2 GeV) MSbar
    24    1.27000000e+00   # Mcharm(Mcharm) MSbar
    11    5.10998902e-04   # Me(pole)
    13    1.05658357e-01   # Mmu(pole)
Block VCKMIN               # input CKM mixing matrix parameters
     1    2.27200000e-01   # lambda_W
     2    8.18000000e-01   # A
     3    2.21000000e-01   # rhobar
     4    3.40000000e-01   # etabar (no phases used in SOFTSUSY yet though)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    1.25000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.58174317e+16   # MX scale
Block RVLAMUDDIN          # input LQD couplings at MSUSY
  1 2 3   1.00000000e-04   # lambda''_{123}
  1 3 2  -1.00000000e-04   # lambda''_{132}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=7.18837093e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.05003164e+01   # MW
        25     1.14769967e+02   # CP even neutral scalar
        35     3.50852190e+02   # CP even neutral scalar
        36     3.50852190e+02   # CP odd neutral scalar
        37     2.22530493e+02   # charged scalar
   1000021     1.14758759e+03   # ~g
   1000022     2.05312077e+02   # ~neutralino(1)
   1000023     3.86888834e+02   # ~neutralino(2)
   1000024     3.86905228e+02   # ~chargino(1)
   1000025    -6.41583915e+02   # ~neutralino(3)
   1000035     6.54958851e+02   # ~neutralino(4)
   1000037     6.55287232e+02   # ~chargino(2)
   1000011     2.29698710e+02   # charged scalar
   1000013     2.29721290e+02   # charged scalar
   1000015     3.60795863e+02   # charged scalar
   2000011     3.60800543e+02   # charged scalar
   2000013     3.61213490e+02   # charged scalar
   2000015     7.20394972e+02   # charged scalar
   1000012     3.51857684e+02   # CP even neutral scalar
   1000014     3.51861023e+02   # CP even neutral scalar
   1000016     7.15653437e+02   # CP even neutral scalar
   1000017     3.51857684e+02   # CP odd neutral scalar
   1000018     3.51861023e+02   # CP odd neutral scalar
   1000019     7.15653437e+02   # CP odd neutral scalar
   1000001     9.67146615e+02   # ~d_1
   1000003     1.00410702e+03   # ~d_2
   1000005     1.01148438e+03   # ~d_3
   2000001     1.01148799e+03   # ~d_4
   2000003     1.05572745e+03   # ~d_5
   2000005     1.05574607e+03   # ~d_6
   1000002     8.06780747e+02   # ~u_1
   1000004     1.00252906e+03   # ~u_2
   1000006     1.01478237e+03   # ~u_3
   2000002     1.01478804e+03   # ~u_4
   2000004     1.05290113e+03   # ~u_5
   2000006     1.05290465e+03   # ~u_6
        12     0.00000000e+00   # Mnu1 inverted hierarchy output
        14     0.00000000e+00   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    0.00000000e+00   # N_{12}
  1 3    0.00000000e+00   # N_{13}
  1 4    0.00000000e+00   # N_{14}
  1 5    0.00000000e+00   # N_{15}
  1 6    0.00000000e+00   # N_{16}
  1 7    0.00000000e+00   # N_{17}
  2 1    0.00000000e+00   # N_{21}
  2 2    0.00000000e+00   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4    0.00000000e+00   # N_{24}
  2 5    0.00000000e+00   # N_{25}
  2 6    0.00000000e+00   # N_{26}
  2 7    0.00000000e+00   # N_{27}
  3 1    0.00000000e+00   # N_{31}
  3 2    0.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4    0.00000000e+00   # N_{34}
  3 5    0.00000000e+00   # N_{35}
  3 6    0.00000000e+00   # N_{36}
  3 7    0.00000000e+00   # N_{37}
  4 1    0.00000000e+00   # N_{41}
  4 2    0.00000000e+00   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    0.00000000e+00   # N_{44}
  4 5    0.00000000e+00   # N_{45}
  4 6    0.00000000e+00   # N_{46}
  4 7    0.00000000e+00   # N_{47}
  5 1    0.00000000e+00   # N_{51}
  5 2    0.00000000e+00   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    0.00000000e+00   # N_{54}
  5 5    0.00000000e+00   # N_{55}
  5 6    0.00000000e+00   # N_{56}
  5 7    0.00000000e+00   # N_{57}
  6 1    0.00000000e+00   # N_{61}
  6 2    0.00000000e+00   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4    0.00000000e+00   # N_{64}
  6 5    0.00000000e+00   # N_{65}
  6 6    0.00000000e+00   # N_{66}
  6 7    0.00000000e+00   # N_{67}
  7 1    0.00000000e+00   # N_{71}
  7 2    0.00000000e+00   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    0.00000000e+00   # N_{74}
  7 5    0.00000000e+00   # N_{75}
  7 6    0.00000000e+00   # N_{76}
  7 7    0.00000000e+00   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    0.00000000e+00   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    0.00000000e+00   # U_{14}
  1 5    0.00000000e+00   # U_{15}
  2 1    0.00000000e+00   # U_{21}
  2 2    1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4    0.00000000e+00   # U_{24}
  2 5    0.00000000e+00   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1    0.00000000e+00   # U_{41}
  4 2    0.00000000e+00   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4   -9.60099519e-01   # U_{44}
  4 5    2.79658565e-01   # U_{45}
  5 1    0.00000000e+00   # U_{51}
  5 2    0.00000000e+00   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4   -2.79658565e-01   # U_{54}
  5 5   -9.60099519e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2    0.00000000e+00   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5    0.00000000e+00   # V_{15}
  2 1    0.00000000e+00   # V_{21}
  2 2    1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4    0.00000000e+00   # V_{24}
  2 5    0.00000000e+00   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1    0.00000000e+00   # V_{41}
  4 2    0.00000000e+00   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4   -9.83228845e-01   # V_{44}
  4 5    1.82376090e-01   # V_{45}
  5 1    0.00000000e+00   # V_{51}
  5 2    0.00000000e+00   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4   -1.82376090e-01   # V_{54}
  5 5   -9.83228845e-01   # V_{55}
Block gauge Q= 8.76220269e+02  # SM gauge couplings
     1     3.62703232e-01   # g'(Q)MSSM DRbar
     2     6.42357191e-01   # g(Q)MSSM DRbar
     3     1.06432994e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.76220269e+02   # diagonal Up Yukawa matrix
  1  1     7.33179837e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.35849916e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.57821195e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 8.76220269e+02   # diagonal down Yukawa matrix
  1  1     1.41236810e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.09240175e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.34889355e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 8.76220269e+02   # diagonal lepton Yukawa matrix
  1  1     2.79077047e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.77043620e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00319812e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 8.76220269e+02 # Higgs mixing parameters
     1     6.36136668e+02    # mu(Q)MSSM DRbar
     2     9.67533422e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44501979e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.31425607e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 8.76220269e+02 # non-zero R-Parity violating LLE couplings 
Block RVLAMLQD Q= 8.76220269e+02 # non-zero R-Parity violating LQD couplings 
Block RVLAMUDD Q= 8.76220269e+02 # non-zero R-Parity violating UDD couplings 
  1 1 2    3.94685818e-19   # lambda''_{112}
  1 1 3    3.90298949e-22   # lambda''_{113}
  1 2 1   -3.94685818e-19   # lambda''_{121}
  1 2 3    1.00000986e-04   # lambda''_{123}
  1 3 1   -3.90298949e-22   # lambda''_{131}
  1 3 2   -1.00000986e-04   # lambda''_{132}
  2 1 2   -8.06039084e-27   # lambda''_{212}
  2 1 3   -7.84097408e-30   # lambda''_{213}
  2 2 1    8.06039084e-27   # lambda''_{221}
  2 2 3    3.78730207e-14   # lambda''_{223}
  2 3 1    7.84097408e-30   # lambda''_{231}
  2 3 2   -3.78730207e-14   # lambda''_{232}
  3 1 2    1.87016621e-25   # lambda''_{312}
  3 1 3    1.81917375e-28   # lambda''_{313}
  3 2 1   -1.87016621e-25   # lambda''_{321}
  3 2 3   -8.87728178e-13   # lambda''_{323}
  3 3 1   -1.81917375e-28   # lambda''_{331}
  3 3 2    8.87728178e-13   # lambda''_{332}
Block RVTLLE Q= 8.76220269e+02 # non-zero R-Parity violating LLE soft terms 
Block RVTLQD Q= 8.76220269e+02 # non-zero R-Parity violating LQD soft terms 
Block RVTUDD Q= 8.76220269e+02 # non-zero R-Parity violating UDD soft terms 
  1 1 2    2.68911749e-15   # T''_{112}
  1 1 3    2.64086963e-18   # T''_{113}
  1 2 1   -2.68911749e-15   # T''_{121}
  1 2 3   -2.15663950e-06   # T''_{123}
  1 3 1   -2.64086963e-18   # T''_{131}
  1 3 2    2.15663950e-06   # T''_{132}
  2 1 2    1.01403466e-22   # T''_{212}
  2 1 3    9.86063656e-26   # T''_{213}
  2 2 1   -1.01403466e-22   # T''_{221}
  2 2 3   -6.81767520e-11   # T''_{223}
  2 3 1   -9.86063656e-26   # T''_{231}
  2 3 2    6.81767520e-11   # T''_{232}
  3 1 2   -2.34687580e-21   # T''_{312}
  3 1 3   -2.28195527e-24   # T''_{313}
  3 2 1    2.34687580e-21   # T''_{321}
  3 2 3    1.59172188e-09   # T''_{323}
  3 3 1    2.28195527e-24   # T''_{331}
  3 3 2   -1.59172188e-09   # T''_{332}
Block RVKAPPA Q= 8.76220269e+02 # R-Parity violating kappa 
     1    0.00000000e+00   # kappa_{1}
     2    0.00000000e+00   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 8.76220269e+02 # R-Parity violating D 
     1    0.00000000e+00   # D_{1}
     2    0.00000000e+00   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 8.76220269e+02 # sneutrino VEVs D 
     1    0.00000000e+00   # SneutrinoVev_{1}
     2    0.00000000e+00   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 8.76220269e+02 # M2LH1 
     1    0.00000000e+00   # M2LH1_{1}
     2    0.00000000e+00   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     0.00000000e+00   # UPMNS_{11} matrix element
  1  2     0.00000000e+00   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1     0.00000000e+00   # UPMNS_{21} matrix element
  2  2     0.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     0.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 8.76220269e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     1.03725641e+06    # (m^_Q^2)_{11}
  1  2     3.57018305e+01    # (m^_Q^2)_{12}
  1  3    -8.43985930e+02    # (m^_Q^2)_{13}
  2  1     3.57018305e+01    # (m^_Q^2)_{21}
  2  2     1.03699768e+06    # (m^_Q^2)_{22}
  2  3     6.21358985e+03    # (m^_Q^2)_{23}
  3  1    -8.43985930e+02    # (m^_Q^2)_{31}
  3  2     6.21358985e+03    # (m^_Q^2)_{32}
  3  3     8.82909605e+05    # (m^_Q^2)_{33}
Block msl2 Q= 8.76220269e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     1.24792268e+05    # (m^_L^2)_{11}
  1  2     0.00000000e+00    # (m^_L^2)_{12}
  1  3     0.00000000e+00    # (m^_L^2)_{13}
  2  1     0.00000000e+00    # (m^_L^2)_{21}
  2  2     1.24789944e+05    # (m^_L^2)_{22}
  2  3     0.00000000e+00    # (m^_L^2)_{23}
  3  1     0.00000000e+00    # (m^_L^2)_{31}
  3  2     0.00000000e+00    # (m^_L^2)_{32}
  3  3     1.24090706e+05    # (m^_L^2)_{33}
Block msd2 Q= 8.76220269e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     9.52928636e+05    # (m^_d^2)_{11}
  1  2    -2.56063524e-06    # (m^_d^2)_{12}
  1  3     2.65132702e-03    # (m^_d^2)_{13}
  2  1    -2.56063524e-06    # (m^_d^2)_{21}
  2  2     9.52923335e+05    # (m^_d^2)_{22}
  2  3    -4.27384951e-01    # (m^_d^2)_{23}
  3  1     2.65132702e-03    # (m^_d^2)_{31}
  3  2    -4.27384951e-01    # (m^_d^2)_{32}
  3  3     9.43296751e+05    # (m^_d^2)_{33}
Block msu2 Q= 8.76220269e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     9.61895740e+05    # (m^_u^2)_{11}
  1  2     1.30617260e-03    # (m^_u^2)_{12}
  1  3    -4.45173887e-05    # (m^_u^2)_{13}
  2  1     1.30617260e-03    # (m^_u^2)_{21}
  2  2     9.61890322e+05    # (m^_u^2)_{22}
  2  3    -5.70236945e-02    # (m^_u^2)_{23}
  3  1    -4.45173887e-05    # (m^_u^2)_{31}
  3  2    -5.70236945e-02    # (m^_u^2)_{32}
  3  3     6.55128657e+05    # (m^_u^2)_{33}
Block mse2 Q= 8.76220269e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     4.92077254e+04    # (m^_e^2)_{11}
  1  2     0.00000000e+00    # (m^_e^2)_{12}
  1  3     0.00000000e+00    # (m^_e^2)_{13}
  2  1     0.00000000e+00    # (m^_e^2)_{21}
  2  2     4.92029859e+04    # (m^_e^2)_{22}
  2  3     0.00000000e+00    # (m^_e^2)_{23}
  3  1     0.00000000e+00    # (m^_e^2)_{31}
  3  2     0.00000000e+00    # (m^_e^2)_{32}
  3  3     4.77770985e+04    # (m^_e^2)_{33}
Block tu Q= 8.76220269e+02   # super CKM trilinear matrix - DRbar
  1  1    -8.38404261e-03    # (T^_u)_{11}
  1  2    -1.65926111e-08    # (T^_u)_{12}
  1  3    -8.99470249e-08    # (T^_u)_{13}
  2  1    -8.27952227e-06    # (T^_u)_{21}
  2  2    -3.84053640e+00    # (T^_u)_{22}
  2  3    -3.91127654e-04    # (T^_u)_{23}
  3  1    -1.11163576e-02    # (T^_u)_{31}
  3  2    -1.17984298e-01    # (T^_u)_{32}
  3  3    -7.60422844e+02    # (T^_u)_{33}
Block td Q= 8.76220269e+02   # super CKM trilinear matrix - DRbar
  1  1    -1.97008251e-01    # (T^_d)_{11}
  1  2    -2.91217840e-06    # (T^_d)_{12}
  1  3     6.92114386e-05    # (T^_d)_{13}
  2  1    -6.37623560e-05    # (T^_d)_{21}
  2  2    -4.31307460e+00    # (T^_d)_{22}
  2  3    -1.11566139e-02    # (T^_d)_{23}
  3  1     6.59728644e-02    # (T^_d)_{31}
  3  2    -4.85706025e-01    # (T^_d)_{32}
  3  3    -1.75998776e+02    # (T^_d)_{33}
Block te Q= 8.76220269e+02   # super CKM trilinear matrix - DRbar
  1  1    -8.30029731e-03    # (T^_e)_{11}
  1  2     0.00000000e+00    # (T^_e)_{12}
  1  3     0.00000000e+00    # (T^_e)_{13}
  2  1     0.00000000e+00    # (T^_e)_{21}
  2  2    -1.71620985e+00    # (T^_e)_{22}
  2  3     0.00000000e+00    # (T^_e)_{23}
  3  1     0.00000000e+00    # (T^_e)_{31}
  3  2     0.00000000e+00    # (T^_e)_{32}
  3  3    -2.96754837e+01    # (T^_e)_{33}
Block VCKM Q= 8.76220269e+02 # DRbar CKM mixing matrix
  1  1     9.73840718e-01    # CKM_{11} matrix element
  1  2     2.27197409e-01    # CKM_{12} matrix element
  1  3     3.94887731e-03    # CKM_{13} matrix element
  2  1    -2.27161573e-01    # CKM_{21} matrix element
  2  2     9.72961269e-01    # CKM_{22} matrix element
  2  3     4.17610938e-02    # CKM_{23} matrix element
  3  1     5.64590762e-03    # CKM_{31} matrix element
  3  2    -4.15656867e-02    # CKM_{32} matrix element
  3  3     9.99119821e-01    # CKM_{33} matrix element
Block msoft Q= 8.76220269e+02 # MSSM DRbar SUSY breaking parameters
     1     2.10406831e+02     # M_1(Q)
     2     3.89202336e+02     # M_2(Q)
     3     1.11364038e+03     # M_3(Q)
    21     1.08623263e+05     # mH1^2(Q)
    22    -3.80244556e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     2.22383949e-05   # (USQMIX)_{11}
  1  2     2.35484513e-04   # (USQMIX)_{12}
  1  3     4.29694480e-01   # (USQMIX)_{13}
  1  4     2.13122729e-10   # (USQMIX)_{14}
  1  5     6.46264838e-07   # (USQMIX)_{15}
  1  6     9.02974306e-01   # (USQMIX)_{16}
  2  1     1.63629534e-04   # (USQMIX)_{21}
  2  2     1.73195267e-03   # (USQMIX)_{22}
  2  3     9.02972787e-01   # (USQMIX)_{23}
  2  4     9.87731228e-09   # (USQMIX)_{24}
  2  5     5.03905571e-05   # (USQMIX)_{25}
  2  6    -4.29694213e-01   # (USQMIX)_{26}
  3  1     1.58685412e-07   # (USQMIX)_{31}
  3  2     8.86171672e-03   # (USQMIX)_{32}
  3  3    -6.05329950e-05   # (USQMIX)_{33}
  3  4    -1.13597381e-04   # (USQMIX)_{34}
  3  5     9.99960726e-01   # (USQMIX)_{35}
  3  6     2.57788662e-05   # (USQMIX)_{36}
  4  1     1.93461263e-05   # (USQMIX)_{41}
  4  2     1.00716377e-06   # (USQMIX)_{42}
  4  3    -1.89310871e-08   # (USQMIX)_{43}
  4  4     9.99999993e-01   # (USQMIX)_{44}
  4  5     1.13592912e-04   # (USQMIX)_{45}
  4  6     7.95222131e-09   # (USQMIX)_{46}
  5  1     1.87878188e-01   # (USQMIX)_{51}
  5  2     9.82152215e-01   # (USQMIX)_{52}
  5  3    -1.66453587e-03   # (USQMIX)_{53}
  5  4    -3.63522165e-06   # (USQMIX)_{54}
  5  5    -8.70404123e-03   # (USQMIX)_{55}
  5  6     5.31341536e-04   # (USQMIX)_{56}
  6  1     9.82192323e-01   # (USQMIX)_{61}
  6  2    -1.87870812e-01   # (USQMIX)_{62}
  6  3     1.58239133e-04   # (USQMIX)_{63}
  6  4    -1.90015035e-05   # (USQMIX)_{64}
  6  5     1.66477616e-03   # (USQMIX)_{65}
  6  6    -5.04967545e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.59225437e-03   # (DSQMIX)_{11}
  1  2    -3.38095929e-02   # (DSQMIX)_{12}
  1  3     9.74056211e-01   # (DSQMIX)_{13}
  1  4     9.71588825e-07   # (DSQMIX)_{14}
  1  5    -1.56628849e-04   # (DSQMIX)_{15}
  1  6     2.23719236e-01   # (DSQMIX)_{16}
  2  1    -1.78771955e-03   # (DSQMIX)_{21}
  2  2     1.31631704e-02   # (DSQMIX)_{22}
  2  3    -2.23387718e-01   # (DSQMIX)_{23}
  2  4    -2.43266160e-06   # (DSQMIX)_{24}
  2  5     3.92325279e-04   # (DSQMIX)_{25}
  2  6     9.74639066e-01   # (DSQMIX)_{26}
  3  1     1.97141563e-06   # (DSQMIX)_{31}
  3  2     4.52076653e-03   # (DSQMIX)_{32}
  3  3     4.02967413e-04   # (DSQMIX)_{33}
  3  4     5.56008489e-06   # (DSQMIX)_{34}
  3  5     9.99989631e-01   # (DSQMIX)_{35}
  3  6    -3.71221856e-04   # (DSQMIX)_{36}
  4  1     2.07140404e-04   # (DSQMIX)_{41}
  4  2     6.48366321e-08   # (DSQMIX)_{42}
  4  3    -2.50183078e-06   # (DSQMIX)_{43}
  4  4     9.99999979e-01   # (DSQMIX)_{44}
  4  5    -5.55898048e-06   # (DSQMIX)_{45}
  4  6     2.30384743e-06   # (DSQMIX)_{46}
  5  1    -1.38066929e-01   # (DSQMIX)_{51}
  5  2     9.89735749e-01   # (DSQMIX)_{52}
  5  3     3.62249407e-02   # (DSQMIX)_{53}
  5  4     2.86129805e-05   # (DSQMIX)_{54}
  5  5    -4.49070957e-03   # (DSQMIX)_{55}
  5  6    -5.31572840e-03   # (DSQMIX)_{56}
  6  1     9.90410620e-01   # (DSQMIX)_{61}
  6  2     1.38153366e-01   # (DSQMIX)_{62}
  6  3     1.30246534e-04   # (DSQMIX)_{63}
  6  4    -2.05166131e-04   # (DSQMIX)_{64}
  6  5    -6.26576556e-04   # (DSQMIX)_{65}
  6  6    -1.91035532e-05   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.45634882e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.89338406e-01   # C_{18}
  2 1    0.00000000e+00   # C_{21}
  2 2    0.00000000e+00   # C_{22}
  2 3    0.00000000e+00   # C_{23}
  2 4    8.73902473e-03   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    0.00000000e+00   # C_{26}
  2 7    9.99961814e-01   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1    0.00000000e+00   # C_{31}
  3 2    0.00000000e+00   # C_{32}
  3 3    4.22709889e-05   # C_{33}
  3 4    0.00000000e+00   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    9.99999999e-01   # C_{36}
  3 7    0.00000000e+00   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    0.00000000e+00   # C_{41}
  4 2    0.00000000e+00   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4    0.00000000e+00   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -4.22709889e-05   # C_{46}
  4 7    0.00000000e+00   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    0.00000000e+00   # C_{51}
  5 2    0.00000000e+00   # C_{52}
  5 3    0.00000000e+00   # C_{53}
  5 4    9.99961814e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    0.00000000e+00   # C_{56}
  5 7   -8.73902473e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.89338406e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.45634882e-01   # C_{68}
  7 1    9.94700974e-01   # C_{71}
  7 2    1.02810375e-01   # C_{72}
  7 3    0.00000000e+00   # C_{73}
  7 4    0.00000000e+00   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6    0.00000000e+00   # C_{76}
  7 7    0.00000000e+00   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    4.71575326e-01   # curlyN_{11}
  1 2    8.81825783e-01   # curlyN_{12}
  1 3    0.00000000e+00   # curlyN_{13}
  1 4    0.00000000e+00   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    0.00000000e+00   # curlyN_{31}
  3 2    0.00000000e+00   # curlyN_{32}
  3 3    0.00000000e+00   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1    0.00000000e+00   # curlyN_{41}
  4 2    0.00000000e+00   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    0.00000000e+00   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    8.81825783e-01   # curlyN_{51}
  5 2   -4.71575326e-01   # curlyN_{52}
  5 3    0.00000000e+00   # curlyN_{53}
  5 4    0.00000000e+00   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1    0.00000000e+00   # curlyN~_{21}
  2 2    0.00000000e+00   # curlyN~_{22}
  2 3    0.00000000e+00   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1    0.00000000e+00   # curlyN~_{31}
  3 2    0.00000000e+00   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    0.00000000e+00   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    8.83985544e-01   # curlyN~_{41}
  4 2    4.67514233e-01   # curlyN~_{42}
  4 3    0.00000000e+00   # curlyN~_{43}
  4 4    0.00000000e+00   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}