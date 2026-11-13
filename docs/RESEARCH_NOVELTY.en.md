# Technology-prior-art overview — Aurora MVP

This comparison summarizes the five technologies covered by the Portuguese matrix in [`RESEARCH_NOVELTY.md`](RESEARCH_NOVELTY.md). It treats the Aurora capabilities in the original brief as a proposed scope; the comparison does not assume that they are already implemented or validated.

| Technology | Documented scope | Factual relationship to the proposed Aurora MVP |
|---|---|---|
| Google Earth Engine | Public Earth-observation catalog and managed distributed geospatial computation, including machine-learning tools, export and interactive/batch workflows. Its quotas, terms and pricing depend on usage category and tier. [1] | Overlaps in geospatial data and analysis. GEE is documented as a broad catalog and managed computation service, while the proposal describes an application-oriented organization, explainability and a modular Gradio interface. This is not a performance comparison. |
| Microsoft Planetary Computer | The public catalog offers Earth/environmental datasets, STAC discovery and asset access. Planetary Computer Pro is a separate Azure product with managed STAC GeoCatalogs and ingestion for customer data. Terms, access methods and costs differ by service and dataset. [2] | Overlaps in discovery and metadata. The closest documented customer-data ingestion functionality belongs to the separate Pro product. The sources do not establish the proposed Aurora as an equivalent catalog service. |
| TorchGeo | A PyTorch-oriented geospatial ML library with datasets, spatial/temporal samplers, transforms, models and pretrained weights. Dataset licenses vary. [3] | Potentially complementary as a source of data and model components for a geospatial application. TorchGeo is a library, not a ready-made Gradio catalog or general explanation layer. |
| SamGeo | An open geospatial adaptation layer for Segment Anything workflows with prompt-based or automatic masks, geospatial exports, maps and APIs. Package, model and checkpoint licenses must be distinguished; large workflows may require substantial GPU memory. [4] | Overlaps in geospatial image segmentation. The cited scope does not establish a general metadata-management or model-explanation application matching the Aurora proposal. |
| NASA–IBM Prithvi | A family of Earth-observation foundation models, including HLS-oriented pretrained weights, code and downstream fine-tuning examples. Model inputs, licensing, size and suitability are checkpoint-specific. [5] | Could be a model component in a compatible application, but is not itself a general image catalog, Gradio workflow manager or causal-explanation system. |

## Conclusion

Existing systems cover important parts of this problem space: managed data discovery and computation, reusable geospatial ML libraries, prompt-based segmentation, and Earth-observation foundation models. These tools differ in scope and are not interchangeable. The available evidence supports partial overlap and possible complementarity, not a validated implementation-level comparison of Aurora. It does **not** support claims that Aurora is the first of its kind, globally novel, superior, equivalent in function, or patentable. A narrower assessment would require a frozen Aurora version, inspectable code, benchmark data and an appropriate technical/legal review.

## References

[1]: https://developers.google.com/earth-engine/guides "Google Earth Engine documentation"
[2]: https://planetarycomputer.microsoft.com/docs/concepts/data-catalog/ "Microsoft Planetary Computer data catalog"
[3]: https://docs.torchgeo.org/en/stable/ "TorchGeo documentation"
[4]: https://samgeo.gishub.org/ "SamGeo documentation"
[5]: https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL "Prithvi-EO-2.0-300M-TL model card"
