
import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';
export default [
{
  path: '/',
  component: ComponentCreator('/','deb'),
  exact: true,
},
{
  path: '/blog',
  component: ComponentCreator('/blog','e84'),
  exact: true,
},
{
  path: '/blog/hello-world',
  component: ComponentCreator('/blog/hello-world','4b5'),
  exact: true,
},
{
  path: '/blog/hola',
  component: ComponentCreator('/blog/hola','1be'),
  exact: true,
},
{
  path: '/blog/tags',
  component: ComponentCreator('/blog/tags','6dc'),
  exact: true,
},
{
  path: '/blog/tags/docusaurus',
  component: ComponentCreator('/blog/tags/docusaurus','8f0'),
  exact: true,
},
{
  path: '/blog/tags/facebook',
  component: ComponentCreator('/blog/tags/facebook','316'),
  exact: true,
},
{
  path: '/blog/tags/hello',
  component: ComponentCreator('/blog/tags/hello','3c5'),
  exact: true,
},
{
  path: '/blog/tags/hola',
  component: ComponentCreator('/blog/tags/hola','81e'),
  exact: true,
},
{
  path: '/blog/welcome',
  component: ComponentCreator('/blog/welcome','b3b'),
  exact: true,
},
{
  path: '/docs',
  component: ComponentCreator('/docs','046'),
  
  routes: [
{
  path: '/docs/',
  component: ComponentCreator('/docs/','87d'),
  exact: true,
},
{
  path: '/docs/creating_plates_1',
  component: ComponentCreator('/docs/creating_plates_1','b9a'),
  exact: true,
},
{
  path: '/docs/doc2',
  component: ComponentCreator('/docs/doc2','fd3'),
  exact: true,
},
{
  path: '/docs/doc3',
  component: ComponentCreator('/docs/doc3','e02'),
  exact: true,
},
{
  path: '/docs/installation',
  component: ComponentCreator('/docs/installation','b2a'),
  exact: true,
},
{
  path: '/docs/mdx',
  component: ComponentCreator('/docs/mdx','955'),
  exact: true,
},
{
  path: '/docs/reference/platemap/plate',
  component: ComponentCreator('/docs/reference/platemap/plate','7e5'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/add_volume',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/add_volume','26e'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/remove_volume',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/remove_volume','759'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/transfer',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/transfer','854'),
  exact: true,
},
]
},
{
  path: '*',
  component: ComponentCreator('*')
}
];
