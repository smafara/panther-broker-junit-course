import { defineMermaidSetup } from '@slidev/types'

export default defineMermaidSetup(() => ({
  theme: 'base',
  fontFamily: 'Arial, sans-serif',
  themeVariables: {
    background: '#101827',
    primaryColor: '#17283b',
    primaryTextColor: '#f1f5f9',
    primaryBorderColor: '#34d9bc',
    secondaryColor: '#243049',
    tertiaryColor: '#1c2540',
    lineColor: '#a4bad1',
    textColor: '#f1f5f9',
    edgeLabelBackground: '#101827',
    clusterBkg: '#111d2d',
    clusterBorder: '#38526b',
    titleColor: '#f1f5f9',
  },
  flowchart: { curve: 'basis', htmlLabels: false, padding: 18 },
}))
