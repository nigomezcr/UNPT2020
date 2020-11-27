#include "drop.hpp"
#include "drop_system.hpp"
#include <string>
#include <fstream>

const int NSTEPS = 55e4;
const double DT = 1e-3;

int main(void) {
  std::vector< std::map< std::string, std::vector<double> > > drops_R_V_F;
  std::vector< std::map< std::string, double> > drops_m_r;

  std::map< std::string, std::vector<double> > vec_R_V_F;
  std::map< std::string, double> vec_m_r;

  vec_R_V_F["R"] = {1, 0, 1.0};
  vec_R_V_F["V"] = {-0.00008, 0.0, 0.0};
  vec_R_V_F["F"] = {0.0, 0.0, 0.0};
  vec_m_r["m"] = 1.0;
  vec_m_r["r"] = 0.43;

  drops_R_V_F.push_back(vec_R_V_F);
  drops_m_r.push_back(vec_m_r);

  vec_R_V_F["R"] = {-1, 2.8*0.000453, 1.};
  vec_R_V_F["V"] = {0.00008, 0.0, 0.0};
  vec_R_V_F["F"] = {0.0, 0.0, 0.0};
  vec_m_r["m"] = 1.0;
  vec_m_r["r"] = 0.43;

  drops_R_V_F.push_back(vec_R_V_F);
  drops_m_r.push_back(vec_m_r);

  drop_system my_system(
    -9.81, 10.0, 33.0, 0.031, 1.0, 0.0005,
    drops_R_V_F, drops_m_r
  );

  // start system
  // my_system.initial_conditions(drops_R_V_F, drops_m_r);
  my_system.compute_force();
  my_system.start_integration(DT);


  // std::string fcsv = "data.csv";
  // std::string ftxt = "data.txt";
  // std::ofstream outcsv(fcsv);
  // std::ofstream outtxt(ftxt);

  std::cout << "t R0_1 R1_1 R2_1 R0_2 R1_2 R2_2\n";

  // evolve
  for(int istep = 0; istep < NSTEPS; ++istep) {
    my_system.time_integration(DT);
    //my_system.compute_force();
    std::cout << istep*DT << " ";
    my_system.print(0);
    my_system.print(1);
    std::cout << "\n";
    // outcsv << my_system.GetDataCSV(istep*DT, 0) << "\n";
    // outtxt << my_system.GetDataTXT(istep*DT, 0) << "\n";

  }

  // outcsv.close();
  // outtxt.close();
  return 0;
}
