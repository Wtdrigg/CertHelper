class CertCoordinates:

    def __init__(self):

        # PDF coordinates used to check which accord format is being used:
        self.verify = (2.73, 0.35, 4.73, 0.46)

        # PDF coordinates to use if format is standard:
        self.standard = {'vendor_name':      (0.85, 8.28, 2.29, 8.34), #x1 was 4.83
                         'insurer_a':        (4.90, 8.55, 7.26, 8.58),
                         'insurer_b':        (4.90, 8.34, 7.26, 8.38),
                         'insurer_c':        (4.90, 8.20, 7.26, 8.22),
                         'insurer_d':        (4.90, 8.06, 7.26, 8.08),
                         'insurer_e':        (4.90, 7.90, 7.26, 7.92),
                         'insurer_f':        (4.90, 7.73, 7.26, 7.75),
                         'agent_name':       (4.82, 9.23, 6.46, 9.27),
                         'agency_name':      (0.30, 9.08, 2.85, 9.10),
                         'agent_phone':      (4.90, 9.04, 6.14, 9.07),
                         'agent_email':      (4.81, 8.88, 5.77, 8.90),
                         'gl_pol_number':    (2.95, 5.75, 4.58, 6.73),
                         'gl_eff_date':      (4.65, 5.82, 5.16, 6.82),
                         'gl_exp_date':      (5.25, 5.84, 5.80, 6.80),
                         'gl_each_occur':    (7.37, 6.73, 8.17, 6.76),
                         'gl_op_agg':        (7.30, 5.87, 7.80, 5.95),
                         'gl_insurer':       (0.27, 5.91, 0.45, 6.81),
                         'al_pol_number':    (2.95, 4.90, 4.58, 5.57),
                         'al_eff_date':      (4.86, 5.02, 4.86, 5.56),
                         'al_exp_date':      (5.25, 4.90, 5.90, 5.57),
                         'al_comb_limit':    (7.29, 5.40, 8.25, 5.57),
                         'al_insurer':       (0.27, 5.07, 0.43, 5.65),
                         'umb_pol_number':   (2.95, 4.40, 4.61, 4.73),
                         'umb_eff_date':     (4.61, 4.40, 5.25, 4.73),
                         'umb_exp_date':     (5.25, 4.40, 5.90, 4.73),
                         'umb_each_occur':   (7.51, 4.71, 8.15, 4.77),
                         'umb_aggregate':    (7.51, 4.55, 8.15, 4.60),
                         'umb_insurer':      (0.27, 4.41, 0.44, 4.81),
                         'wc_pol_number:':   (3.00, 3.72, 4.52, 4.24),
                         'wc_eff_date':      (4.60, 3.80, 5.25, 4.24),
                         'wc_exp_date':      (5.26, 3.80, 5.90, 4.24),
                         'wc_each_acci':     (7.31, 4.00, 8.25, 4.07),
                         'wc_each_emp':      (7.31, 3.85, 8.24, 3.90),
                         'wc_pol_limit':     (7.43, 3.74, 8.12, 3.76),
                         'wc_insurer':       (0.28, 3.84, 0.43, 4.32),
                         }

        # PDF coordinates to use if format is alternate:
        self.alternate = {'insurer_a':        (),
                          'insurer_b':        (),
                          'insurer_c':        (),
                          'insurer_d':        (),
                          'insurer_e':        (),
                          'insurer_f':        (),
                          'agent_name':       (),
                          'agency_name':      (),
                          'agent_phone':      (),
                          'agent_email':      (),
                          'gl_pol_number':    (),
                          'gl_eff_date':      (),
                          'gl_exp_date':      (),
                          'gl_each_occur':    (),
                          'gl_op_agg':        (),
                          'gl_insurer':       (),
                          'al_pol_number':    (),
                          'al_eff_date':      (),
                          'al_exp_date':      (),
                          'al_comb_limit':    (),
                          'al_insurer':       (),
                          'umb_pol_number':   (),
                          'umb_eff_date':     (),
                          'umb_exp_date':     (),
                          'umb_each_occur':   (),
                          'umb_aggregate':    (),
                          'umb_insurer':      (),
                          'wc_pol_number:':   (),
                          'wc_eff_date':      (),
                          'wc_exp_date':      (),
                          'wc_each_acci':     (),
                          'wc_each_emp':      (),
                          'wc_pol_limit':     (),
                          'wc_insurer':       (),
                          }
