#include "globals.hh"
#include <string>

/* Module definitions for CAD models */
using namespace std;
class CADModuleDefinition
{
    CADModuleDefinition()
    {
        /* Single module layer stackup */
        hex_module_single.emplace_back({"G4_Galactic", 0.50 * mm, "6in-PCBcover-single-050mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.60 * mm, "6in-PCBcover-spacers-single-160mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.50 * mm, "6in-ModWithSkiroc-components-single-150mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.20 * mm, "6in-ModWithSkiroc-board-single-120mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.20 * mm, "6in-PCB128-single-120mm.STL"});
        hex_module_single.emplace_back({"Si", 0.30 * mm, "6in-sensor-physical-single-030mm.STL"});
        hex_module_single.emplace_back({"G4_KAPTON", 0.05 * mm, "6in-kapton-single-005mm.STL"});
        hex_module_single.emplace_back({"G4_Ag", 0.02 * mm, "6in-gold-layer-single-002mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 0.05 * mm,"6in-adhesive-sensor-single-005mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 0.05 *  mm ,"6in-adhesive-baseplate-single-005mm.STL"});
        hex_module_single.emplace_back({"WCu", 1.20 * mm,"6in-baseplate-single-120mm.STL"});

        /* Cluster module layer stackup */
        hex_module_single.emplace_back({"G4_Galactic", 0.50 * mm, "6in-PCBcover-cluster-050mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.60 * mm, "6in-PCBcover-spacers-cluster-160mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.50 * mm, "6in-ModWithSkiroc-components-cluster-150mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.20 * mm, "6in-ModWithSkiroc-board-cluster-120mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 1.20 * mm, "6in-PCB128-cluster-120mm.STL"});
        hex_module_single.emplace_back({"Si", 0.30 * mm, "6in-sensor-physical-cluster-030mm.STL"});
        hex_module_single.emplace_back({"G4_KAPTON", 0.05 * mm, "6in-kapton-cluster-005mm.STL"});
        hex_module_single.emplace_back({"G4_Ag", 0.02 * mm, "6in-gold-layer-cluster-002mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 0.05 * mm,"6in-adhesive-sensor-cluster-005mm.STL"});
        hex_module_single.emplace_back({"G4_Galactic", 0.05 *  mm ,"6in-adhesive-baseplate-cluster-005mm.STL"});
        hex_module_single.emplace_back({"WCu", 1.20 * mm,"6in-baseplate-cluster-120mm.STL"});
    }
private:
    typedef struct cad_layer
    {
        string material;
        double thickness;
        string filename;
    } cad_layer;

    std::vector<cad_layer> hex_module_single;
    std::vector<cad_layer> hex_module_cluster;

}


