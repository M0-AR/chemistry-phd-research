"""Ch 22: coordination helpers."""
def oxidation_state_complex(net_charge: int, ligand_charges: list) -> int:
    return net_charge - sum(ligand_charges)
def coordination_number(ligands: list) -> int:
    """ligands: list of denticities, e.g. [2,2,2] for Co(en)3."""
    return sum(ligands)
