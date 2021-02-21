module.exports = {
  title: "Platemap",
  tagline: "A simple and small class to handle microplates / micro titreplates",
  url: "https://Benedict-Carling.github.io",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/platemap.ico",
  organizationName: "Benedict-Carling", // Usually your GitHub org/user name.
  projectName: "platemap", // Usually your repo name.
  themeConfig: {
    colorMode: {
      // "light" | "dark"
      defaultMode: "light",

      // Hides the switch in the navbar
      // Useful if you want to support a single color mode
      disableSwitch: false,

      // Should we use the prefers-color-scheme media-query,
      // using user system preferences, instead of the hardcoded defaultMode
      respectPrefersColorScheme: false,
    },
    navbar: {
      title: "",
      logo: {
        alt: "My Site Logo",
        src: "img/greenlogo.svg",
      },
      items: [
        {
          to: "docs/",
          activeBasePath: "docs",
          label: "Docs",
          position: "left",
        },
        //{ to: "blog", label: "Blog", position: "left" },
        {
          href: "https://pypi.org/project/platemap/",
          label: "PyPi",
          position: "left",
        },
        //{
        //  href: "https://www.londonbiofoundry.org/",
        //  label: "London Biofoundry",
        // position: "left",
        //},
        {
          href: "https://github.com/Benedict-Carling/platemap",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      copyright: `Copyright © ${new Date().getFullYear()} Platemap, Inc. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          editUrl:
            "https://github.com/facebook/docusaurus/edit/master/website/",
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            "https://github.com/facebook/docusaurus/edit/master/website/blog/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
};
